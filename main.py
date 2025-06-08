from tkinter import *
import tkinter.messagebox  
from PIL import Image,ImageTk
import tkinter
from student import Student
import os
from train import Train
from Face_Recognization import Face_recognization
from Attendance import Attendance
from developer import Developer
from help import Help 

class Face_Recognization_System:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1350x660+0+0")
       self.root.title("Face Recognization System")

       #first image
       img=Image.open(r"photos\grp stud.jpg")
       img= img.resize((500, 130), Image.Resampling.LANCZOS)
       self.photoImg= ImageTk.PhotoImage(img)
       f_1b1= Label(self.root,image=self.photoImg)
       f_1b1.place(x=0, y=0, width=380, height=147)

       #second image
       img2=Image.open(r"photos\ab.jpg")
       img2 = img2.resize((600, 160), Image.Resampling.LANCZOS)
       self.photoImg2=ImageTk.PhotoImage(img2)
       f_1b1= Label(self.root,image=self.photoImg2)
       f_1b1.place(x=380, y=0, width=400, height=155)

       #third image
       img3=Image.open(r"photos\tech.jpg")
       img3 = img3.resize((600, 160), Image.Resampling.LANCZOS)
       self.photoImg3=ImageTk.PhotoImage(img3)
       f_1b1= Label(self.root,image=self.photoImg3)
       f_1b1.place(x=760, y=0, width=400, height=155)

       #fourth image
       img4=Image.open(r"photos\aa.jpg")
       img4 = img4.resize((600, 160), Image.Resampling.LANCZOS)
       self.photoImg4=ImageTk.PhotoImage(img4)
       f_1b1= Label(self.root,image=self.photoImg4)
       f_1b1.place(x=1160, y=0, width=380, height=158)

       img5=Image.open(r"photos\cs.jpg")
       img5=img5.resize((2000,710),Image.Resampling. LANCZOS)
       self.photoImg5=ImageTk.PhotoImage(img5)
  
       # Bg image
       bg_img=Label(self.root,image=self.photoImg5)
       bg_img.place(x=0,y=140,width=2000,height=710)

       title_lbl=Label(bg_img,text="Face Recognition Attendance System Software",font=("times new roman",30,"bold"),bg="red",fg="white")
       title_lbl.place(x=0,y=0,width=1540,height=60)   
       
       #student button
       img6=Image.open(r"photos\aab.jpg")
       img6=img6.resize((220,220),Image.Resampling.LANCZOS)
       self.photoImg6=ImageTk.PhotoImage(img6)

       b1 = Button(bg_img, image=self.photoImg6,command=self.student_details, cursor="hand2")
       b1.place(x=200,y=100,width=220,height=220) 

       b1_1=Button(bg_img,text="Student Details",command=self.student_details, cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white") 
       b1_1.place(x=200,y=300,width=220,height=40)

       #face detector button
       img7=Image.open(r"photos\face detector.jpg")
       img7=img7.resize((220,220),Image.Resampling.LANCZOS)
       self.photoImg7=ImageTk.PhotoImage(img7)

       b1=Button(bg_img,image=self.photoImg7,cursor="hand2",command=self.face_data) 
       b1.place(x=500,y=100,width=220,height=220) 

       b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white") 
       b1_1.place(x=500,y=300,width=220,height=40)


      # Attendance face button
       img8=Image.open(r"photos\attendance.jpg")
       img8=img8.resize((220,220),Image.Resampling.LANCZOS)
       self.photoImg8=ImageTk.PhotoImage(img8)

       b1=Button(bg_img,image=self.photoImg8,cursor="hand2",command=self.Attendance_data) 
       b1.place(x=800,y=100,width=220,height=220) 

       b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.Attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white") 
       b1_1.place(x=800,y=300,width=220,height=40) 

       
       # Help face button
       img9=Image.open(r"photos\help.jpg")
       img9=img9.resize((220,220),Image.Resampling.LANCZOS)
       self.photoImg9=ImageTk.PhotoImage(img9)

       b1=Button(bg_img,image=self.photoImg9,cursor="hand2",command=self.Help_data) 
       b1.place(x=1100,y=100,width=220,height=220) 

       b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.Help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white") 
       b1_1.place(x=1100,y=300,width=220,height=40) 

      

       # Train face button
       img10=Image.open(r"photos\train.jpg")
       img10=img10.resize((220,220),Image.Resampling.LANCZOS)
       self.photoImg10=ImageTk.PhotoImage(img10)

       b1=Button(bg_img,image=self.photoImg10,cursor="hand2",command=self.train_data) 
       b1.place(x=200,y=380,width=220,height=220) 

       b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white") 
       b1_1.place(x=200,y=580,width=220,height=40) 
       

       # Photos face button
       img11=Image.open(r"photos\photo.jpg")
       img11=img11.resize((220,220),Image.Resampling.LANCZOS)
       self.photoImg11=ImageTk.PhotoImage(img11)

       b1=Button(bg_img,image=self.photoImg11,cursor="hand2") 
       b1.place(x=500,y=380,width=220,height=220) 

       b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white") 
       b1_1.place(x=500,y=580,width=220,height=40) 
       

       # Developer face button
       img12=Image.open(r"photos\developer.jpg")
       img12=img12.resize((220,220),Image.Resampling.LANCZOS)
       self.photoImg12=ImageTk.PhotoImage(img12)

       b1=Button(bg_img,image=self.photoImg12,cursor="hand2",command=self.Developer_data) 
       b1.place(x=800,y=380,width=220,height=220) 

       b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.Developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white") 
       b1_1.place(x=800,y=580,width=220,height=40) 
       

       # Exit face button
       img13=Image.open(r"photos\exit.jpg")
       img13=img13.resize((220,220),Image.Resampling.LANCZOS)    
       self.photoImg13=ImageTk.PhotoImage(img13)

       b1=Button(bg_img,image=self.photoImg13,cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white") 
       b1.place(x=1100,y=380,width=220,height=220) 

       b1_1=b1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white") 
       b1_1.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("data") 

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognization","Are You Sure Exit This Project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return   

       #functions button
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
                               
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognization(self.new_window)


    def Attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)


    def Developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
     
    def Help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

                             
                           
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognization_System(root)
    root.mainloop()

