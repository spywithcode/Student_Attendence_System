from tkinter import * 
from PIL import Image,ImageTk


class Help:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1350x660+0+0")
       self.root.title("Face Recognization System")

       title_lbl = Label(self.root, text="HELP DESK", font=("Times new roman", 35, "bold"), bg="white", fg="blue")
       title_lbl.place(x=0, y=0, width=1530, height=45)

        # Top image
       img_top = Image.open(r"photos\h2.png")
       img_top = img_top.resize((1530, 720), Image.Resampling.LANCZOS)
       self.photoImg_top = ImageTk.PhotoImage(img_top)
       f_1b1=Label(self.root, image=self.photoImg_top)
       f_1b1.place(x=0, y=55, width=1530, height=720)


       dev_label=Label(f_1b1,text="Email: project123@gmail.com", font=("times new roman", 20, "bold"),bg="White")
       dev_label.place(x=600, y=650)


if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()

