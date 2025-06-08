from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import numpy as np
import cv2

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("Times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Top image
        img_top = Image.open(r"photos\facial.png")
        img_top = img_top.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoImg_top = ImageTk.PhotoImage(img_top)
        Label(self.root, image=self.photoImg_top).place(x=0, y=55, width=1530, height=325)

        # Train button
        Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2",
               font=("times new roman", 30, "bold"), bg="red", fg="white").place(x=0, y=380, width=1530, height=60)

        # Bottom image
        img_bottom = Image.open(r"photos\FR.png")
        img_bottom = img_bottom.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoImg_bottom = ImageTk.PhotoImage(img_bottom)
        Label(self.root, image=self.photoImg_bottom).place(x=0, y=440, width=1530, height=325)

    def train_classifier(self):
        data_dir = r"data"
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", f"Data directory does not exist: {data_dir}")
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []

        for image_path in path:
            filename = os.path.basename(image_path)
            try:
                # Extract ID assuming filename format: user.<id>.<imgno>.jpg
                parts = filename.split('.')
                if len(parts) >= 3 and parts[1].isdigit():
                    id = int(parts[1])
                else:
                    print(f"Invalid filename format: {filename}, skipping.")
                    continue

                img = Image.open(image_path).convert('L')  # grayscale
                imageNp = np.array(img, 'uint8')
                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training", imageNp)
                cv2.waitKey(1)

            except Exception as e:
                print(f"Skipping file {filename}: {e}")

        if len(faces) == 0:
            messagebox.showwarning("Warning", "No valid face data found.")
            return

        ids = np.array(ids)

        # Train the classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training dataset completed successfully!")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()