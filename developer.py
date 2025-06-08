from tkinter import *
from PIL import Image,ImageTk


class Developer:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1350x660+0+0")
       self.root.title("Face Recognization System")

       title_lbl = Label(self.root, text="DEVELOPER", font=("Times new roman", 35, "bold"), bg="white", fg="blue")
       title_lbl.place(x=0, y=0, width=1530, height=45)

        # Top image
       img_top = Image.open(r"photos\devv.jpg")
       img_top = img_top.resize((1530, 720), Image.Resampling.LANCZOS)
       self.photoImg_top = ImageTk.PhotoImage(img_top)
       f_1b1=Label(self.root, image=self.photoImg_top)
       f_1b1.place(x=0, y=55, width=1530, height=720)

       # Frame
       main_frame=Frame(f_1b1,bd=2,bg="white")
       main_frame.place(x=1000, y=0,width=500, height=600)


       img_top1 = Image.open(r"photos\devv.jpg")
       img_top1 = img_top1.resize((200, 200), Image.Resampling.LANCZOS)
       self.photoImg_top1 = ImageTk.PhotoImage(img_top1)
       f_1b1=Label(main_frame, image=self.photoImg_top1)
       f_1b1.place(x=300, y=0, width=200, height=200)

       #developer info
       dev_label=Label(main_frame,text="Hello My Name, John", font=("times new roman", 20, "bold"),bg="White")
       dev_label.place(x=0, y=5)

       dev_label=Label(main_frame,text="We are developed this Software", font=("times new roman", 13, "bold"),bg="White")
       dev_label.place(x=0, y=40)


       img3=Image.open(r"photos\design-team.jpg")
       img3 = img3.resize((500, 390), Image.Resampling.LANCZOS)
       self.photoImg3=ImageTk.PhotoImage(img3)
       f_1b1= Label(main_frame,image=self.photoImg3)
       f_1b1.place(x=0, y=210, width=500, height=390)


if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
