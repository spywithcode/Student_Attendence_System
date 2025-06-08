from tkinter import *
from PIL import Image, ImageTk
import cv2
import pymysql
from datetime import datetime


class Face_recognization:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x660+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("Times New Roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1500, height=45)

        img1 = Image.open(r"photos\Fd.jpg")
        img1 = img1.resize((650, 750), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=55, width=650, height=750)

        img2 = Image.open(r"photos\ffd.jpg")
        img2 = img2.resize((870, 820), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=650, y=55, width=870, height=820)
        
        # Button
        b1_1 = Button(f_lbl2, text="Face Recognition", command=self.face_recog, cursor="hand2",
                      font=("times new roman", 18, "bold"), bg="red", fg="white")
        b1_1.place(x=250, y=620, width=220, height=40)

    def mark_attendance(self, i, r, n, d):
        path = ("College.csv")
        with open(path, "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = [line.split(",")[0] for line in myDataList]

            if i not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
            coord = []

            for (x, y, w, h) in features:
                id, predict = clf.predict(gray[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))
                print(f"Predicted ID: {id}, Confidence: {confidence}%")

                conn = pymysql.connect(host="localhost", user="root", password="root", database="online_student_attendance")
                my_cursor = conn.cursor()

            
                my_cursor.execute("SELECT Name FROM student WHERE Student_id = %s", (str(id),))
                result = my_cursor.fetchone()
                n = result[0] if result else "Unknown"

                my_cursor.execute("SELECT Roll FROM student WHERE Student_id = %s", (str(id), ))
                result = my_cursor.fetchone()
                r = result[0] if result else "Unknown"

                my_cursor.execute("SELECT Dep FROM student WHERE Student_id = %s", (str(id),))
                result = my_cursor.fetchone()
                d = result[0] if result else "Unknown"

                my_cursor.execute("SELECT Student_id FROM student WHERE Student_id = %s", (str(id), ))
                result = my_cursor.fetchone()

                i = result[0] if result else "Unknown"

                if confidence > 77 and i != "Unknown":
                    cv2.putText(img, f"ID: {i}", (x,y-75), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                    cv2.putText(img, f"Name: {n}", (x,y-50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                    cv2.putText(img, f"Roll: {r}", (x,y-25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                    cv2.putText(img, f"Dep: {d}", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                    self.mark_attendance(i, r, n, d)

                    # Show recognized user data in a popup window
                    def show_user_info():
                        info_win = Toplevel(self.root)
                        info_win.title("Student Info")
                        info_win.geometry("350x200")
                        Label(info_win, text=f"ID: {i}", font=("Arial", 14)).pack(pady=5)
                        Label(info_win, text=f"Name: {n}", font=("Arial", 14)).pack(pady=5)
                        Label(info_win, text=f"Roll No: {r}", font=("Arial", 14)).pack(pady=5)
                        Label(info_win, text=f"Department: {d}", font=("Arial", 14)).pack(pady=5)
                        Button(info_win, text="Close", command=info_win.destroy).pack(pady=10)

                    # Call popup only once per recognition
                    if not hasattr(self, 'info_shown') or not self.info_shown:
                        self.info_shown = True
                        self.root.after(100, show_user_info)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.putText(img, "Unknown Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (0, 255, 0), "Face", clf)
            return img

        # Load classifier and model
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        cap = cv2.VideoCapture(0)
        while True:
            ret, img = cap.read()
            if not ret:
                break
            
            img = recognize(img, clf, faceCascade)
            print("Image : ",img)
            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Enter key
                break

        cap.release()
        cv2.destroyAllWindows()
    

if __name__ == "__main__":
    root = Tk()
    obj = Face_recognization(root)
    root.mainloop()
