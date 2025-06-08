from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql
import cv2


class Student:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1350x660+0+0")
       self.root.title("Face Recognization System")

       #variables
       self.var_dep=StringVar()
       self.var_course=StringVar()
       self.var_year=StringVar()
       self.var_semester=StringVar()
       self.var_std_id=StringVar()
       self.var_std_name=StringVar()
       self.var_div=StringVar()
       self.var_roll=StringVar()
       self.var_gender=StringVar()
       self.var_dob=StringVar()
       self.var_email=StringVar()
       self.var_phone=StringVar()
       self.var_address=StringVar()
       self.var_teacher=StringVar()


       #first image
       img=Image.open(r"photos\group face recog.jpg")
       img= img.resize((500, 130), Image.LANCZOS)
       self.photoImg= ImageTk.PhotoImage(img)
       f_1b1= Label(self.root,image=self.photoImg)
       f_1b1.place(x=0, y=0, width=500, height=130)

       #second image
       img2=Image.open(r"photos\grp cr.jpg")
       img2 = img2.resize((500, 130), Image.LANCZOS)
       self.photoImg2=ImageTk.PhotoImage(img2)
       f_1b1= Label(self.root,image=self.photoImg2)
       f_1b1.place(x=500, y=0, width=500, height=130)

       #third image
       img3=Image.open(r"photos\grp stud.jpg")
       img3 = img3.resize((550, 130), Image.LANCZOS)
       self.photoImg3=ImageTk.PhotoImage(img3)
       f_1b1= Label(self.root,image=self.photoImg3)
       f_1b1.place(x=1000, y=0, width=550, height=130)

       #bg_image
       img4=Image.open(r"photos\grp stud.jpg")
       img4=img4.resize((1530,710),Image.LANCZOS)
       self.photoImg4=ImageTk.PhotoImage(img4)

       bg_img=Label(self.root,image=self.photoImg4)
       bg_img.place(x=0,y=130,width=1530,height=710)


       title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
       title_lbl.place(x=0,y=0,width=1530,height=45)


       main_frame=Frame(bg_img,bd=2)
       main_frame.place(x=20, y=50,width=1480, height=600)
       
       #left label frame
       Left_frame=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 15, "bold"))
       Left_frame.place(x=10, y=10, width=730, height=580)

       img5_left=Image.open(r"photos\grp sd.jpg")
       img5_left = img5_left.resize((720, 130), Image.LANCZOS)
       self.photoImg5_left=ImageTk.PhotoImage(img5_left)

       f_1b1= Label(Left_frame,image=self.photoImg5_left)
       f_1b1.place(x=5, y=0, width=720, height=130)


       #current course information
       current_course_frame=LabelFrame(Left_frame,bd=2,bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 15, "bold"))
       current_course_frame.place(x=5, y=135, width=720, height=120)


        # Department
       dep_label=Label(current_course_frame,text="Department:", font=("times new roman", 13, "bold"),bg="White")
       dep_label.grid(row=0, column=0, padx=10, sticky=W)


       dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep, font=("times new roman", 13, "bold"), state="read only")
       dep_combo["values"]=("Select Department", "Computer Science", "Bio-chemistry", "Botany", "Mathematics","Physics","Cyber security","Geology","Electronics","Seed Technology","Chemistry" )
       dep_combo.current(0)
       dep_combo.grid(row=0, column=1, padx=2, pady=10,sticky=W)

       # course
       course_label=Label(current_course_frame, text="Course:", font=("times new roman", 13, "bold"),bg="White")
       course_label.grid(row=0, column=2, padx=10,sticky=W)


       course_combo=ttk.Combobox(current_course_frame, textvariable=self.var_course,font=("times new roman", 13, "bold"), state="read only",width=20)
       course_combo["values"]=("Select Course", "BSc", "BCA", "MSc", "PGDCA")
       course_combo.current(0)
       course_combo.grid(row=0, column=3, padx=2, pady=10,sticky=W)
            

       #Year     
       year_label=Label(current_course_frame, text="Year:", font=("times new roman", 13, "bold"),bg="White")
       year_label.grid(row=1, column=0, padx=10,sticky=W)


       year_combo=ttk.Combobox(current_course_frame, textvariable=self.var_year,font=("times new roman", 13, "bold"), state="read only",width=20)
       year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24","2024-25")
       year_combo.current(0)
       year_combo.grid(row=1, column=1, padx=2, pady=10,sticky=W)
       
       #Semester
       semester_label=Label(current_course_frame, text="Semester:", font=("times new roman", 13, "bold"),bg="White")
       semester_label.grid(row=1, column=2, padx=10,sticky=W)


       semester_combo=ttk.Combobox(current_course_frame, textvariable=self.var_semester,font=("times new roman", 13, "bold"), state="read only",width=20)
       semester_combo["values"]=("Select Semester", "Semester1","Semester2","Semester3","Semester4","Semester5","Semester6","Semester7","Semester8")
       semester_combo.current(0)
       semester_combo.grid(row=1, column=3, padx=2, pady=10,sticky=W)

       # Class Student information
       class_student_frame=LabelFrame(Left_frame,bd=2,bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 15, "bold"))
       class_student_frame.place(x=5, y=260, width=720, height=300)
       

        #Student id
       studentId_label=Label(class_student_frame, text="StudentID:", font=("times new roman", 13, "bold"),bg="White")
       studentId_label.grid(row=0, column=0, padx=10,pady=5,sticky=W)

       studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman", 13, "bold"))
       studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


       #Student name
       studentName_label=Label(class_student_frame, text="Student Name:", font=("times new roman", 13, "bold"),bg="White")
       studentName_label.grid(row=0, column=2, padx=10,pady=5,sticky=W)

       studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman", 13, "bold"))
       studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

       
        #class division
       class_div_label=Label(class_student_frame, text="Class Division:", font=("times new roman", 13, "bold"),bg="White")
       class_div_label.grid(row=1, column=0, padx=10,pady=5,sticky=W)

       div_combo=ttk.Combobox(class_student_frame, textvariable=self.var_div, font=("times new roman",13,"bold"))
       div_combo["values"]=("Select Division","A","B","C")
       div_combo.current(0)
       div_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)


       
       
        # roll_no
       roll_no_label=Label(class_student_frame, text="Roll_no:", font=("times new roman", 13, "bold"),bg="White")
       roll_no_label.grid(row=1, column=2, padx=10,pady=5,sticky=W)

       roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman", 13, "bold"))
       roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
       

        #Gender
       gender_label=Label(class_student_frame, text="Gender:", font=("times new roman", 13, "bold"),bg="White")
       gender_label.grid(row=2, column=0, padx=10,pady=5,sticky=W)

       gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"))
       gender_combo["values"]=("Male","Female")
       gender_combo.current(0)
       gender_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W)


       # Dob
       dob_label=Label(class_student_frame, text="DOB:", font=("times new roman", 13, "bold"),bg="White")
       dob_label.grid(row=2, column=2, padx=10,pady=5,sticky=W)

       dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman", 13, "bold"))
       dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
    

        # Email
       email_label=Label(class_student_frame, text="Email:", font=("times new roman", 13, "bold"),bg="White")
       email_label.grid(row=3, column=0, padx=10,pady=5,sticky=W)

       email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman", 13, "bold"))
       email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
       

        # phone no
       phone_no_label=Label(class_student_frame, text="Phone No:", font=("times new roman", 13, "bold"),bg="White")
       phone_no_label.grid(row=3, column=2, padx=10,pady=5,sticky=W)

       phone_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman", 13, "bold"))
       phone_no_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
  

      # address
       address_label=Label(class_student_frame, text="Address:", font=("times new roman", 13, "bold"),bg="White")
       address_label.grid(row=4, column=0, padx=10,pady=5,sticky=W)

       address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman", 13, "bold"))
       address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
       
        # teacher name
       teacher_name_label=Label(class_student_frame, text="Teacher Name:", font=("times new roman", 13, "bold"),bg="White")
       teacher_name_label.grid(row=4, column=2, padx=10,pady=5,sticky=W)

       teacher_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman", 13, "bold"))
       teacher_name_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

       # radio button 
       self.var_radio1=StringVar()
       radionbtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
       radionbtn1.grid(row=6,column=0)
       
    
       radionbtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="no")
       radionbtn2.grid(row=6,column=1)

       # buttons frame
       btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="WHITE")
       btn_frame.place(x=0,y=200,width=715,height=90)

       save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="White")
       save_btn.grid(row=0,column=0)
        
       
       update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="White")
       update_btn.grid(row=0,column=1)

       delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="White")
       delete_btn.grid(row=0,column=2) 

       reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=20,font=("times new roman",13,"bold"),bg="blue",fg="White")
       reset_btn.grid(row=0,column=3)

       btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="WHITE")
       btn_frame1.place(x=0,y=240,width=715,height=35)

       take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="White")
       take_photo_btn.grid(row=0,column=0)

       update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="White")
       update_photo_btn.grid(row=0,column=1)
       
       #right label frame
       Right_frame=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 20, "bold"))
       Right_frame.place(x=750, y=7, width=720, height=580)

       img6_right=Image.open(r"photos\aa.jpg")
       img6_right = img6_right.resize((720, 130), Image.LANCZOS)
       self.photoimg6_right=ImageTk.PhotoImage(img6_right)

       f_1b1= Label(Right_frame,image=self.photoimg6_right)
       f_1b1.place(x=5, y=0, width=720, height=130)

       #search system

       Search_frame=LabelFrame(Right_frame,bd=2,bg="white", relief=RIDGE, text="Search System ", font=("times new roman", 15, "bold"))
       Search_frame.place(x=5, y=135, width=710, height=70) 
       
       search_label=Label(Search_frame, text="Search By:", font=("times new roman", 13, "bold"),bg="Red",fg="White")
       search_label.grid(row=0, column=0, padx=10,pady=5,sticky=W)

       search_combo=ttk.Combobox(Search_frame, font=("times new roman", 13, "bold"), state="read only",width=15)
       search_combo["values"]=("Select","Roll_No","Phone_No")
       search_combo.current(0)
       search_combo.grid(row=0, column=1, padx=2, pady=10,sticky=W)

       search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman", 13, "bold"))
       search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

       search_btn=Button(Search_frame,text="Search ",width=12,font=("times new roman",12,"bold"),bg="blue",fg="White")
       search_btn.grid(row=0,column=3,padx=4)

       showAll_btn=Button(Search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="White")
       showAll_btn.grid(row=0,column=4,padx=4)
       


       #table frame 
       table_frame=Frame(Right_frame,bd=2,bg="white", relief=RIDGE)
       table_frame.place(x=5, y=210, width=710, height=330) 

       scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
       scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

       self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
       
       scroll_x.pack(side=BOTTOM,fill=X)
       scroll_y.pack(side=RIGHT,fill=Y)
       scroll_x.config(command=self.student_table.xview)
       scroll_y.config(command=self.student_table.yview)

       self.student_table.heading("dep",text="Department")
       self.student_table.heading("course",text="Course")

       self.student_table.heading("year",text="Year")
       self.student_table.heading("sem",text="Semester")
       self.student_table.heading("id",text="StudentId")
       self.student_table.heading("name",text="Name")
       self.student_table.heading("roll",text="Roll No")
       self.student_table.heading("div",text="Division")
       self.student_table.heading("gender",text="Gender")
       self.student_table.heading("dob",text="DOB")
       self.student_table.heading("email",text="Email")
       self.student_table.heading("phone",text="Phone")
       self.student_table.heading("address",text="Address")
       self.student_table.heading("teacher",text="Teacher")
       self.student_table.heading("photo",text="PhotoSampleStatus")   
       self.student_table["show"] ="headings"

       self.student_table.pack(fill=BOTH,expand=1) 
       self.student_table.column("dep",width=100) 
       self.student_table.column("course",width=100)
       self.student_table.column("year",width=100)
       self.student_table.column("sem",width=100)
       self.student_table.column("id",width=100)
       self.student_table.column("name",width=100)
       self.student_table.column("roll",width=100)
       self.student_table.column("div",width=100)
       self.student_table.column("gender",width=100)
       self.student_table.column("dob",width=100)
       self.student_table.column("email",width=100)
       self.student_table.column("phone",width=100)
       self.student_table.column("address",width=100)
       self.student_table.column("teacher",width=100)
       self.student_table.column("photo",width=150)

       self.student_table.bind("<ButtonRelease>",self.get_cursor)
       self.fetch_data()
       

       #function declaration
    def add_data(self):
        """
        Insert a new student record into the database.
        Validates required fields before insertion.
        """
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
            return

        try:
            conn = pymysql.connect(host="localhost", user="root", password="root", database="online_student_attendance")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "INSERT INTO student VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                )
            )
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)  


     # fetch data
    def fetch_data(self):
         conn=pymysql.connect(host="localhost",user="root",password="root",database="online_student_attendance")  
         my_cursor=conn.cursor()
         my_cursor.execute("select * from student")
         data=my_cursor.fetchall()
    
         if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                 self.student_table.insert("",END,values=i)
            conn.commit()
         conn.close() 


    def get_cursor(self, event=""):
      cursor_focus = self.student_table.focus()
      content = self.student_table.item(cursor_focus)
      data = content.get("values", [])

      if len(data) >= 15:
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])
      else:
        print(" Warning: selected row does not have enough data.")


    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details", parent=self.root)
                if Update>0:
                    conn=pymysql.connect(host="localhost",user="root",password="root",database="online_student_attendance")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s, Course=%s, Year=%s ,Semester=%s,name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s",(
                                                                                                         self.var_dep.get(),
                                                                                                         self.var_course.get(),
                                                                                                         self.var_year.get(),
                                                                                                         self.var_semester.get(),
                                                                                                         self.var_std_name.get(),
                                                                                                         self.var_div.get(),
                                                                                                         self.var_roll.get(),
                                                                                                         self.var_gender.get(),
                                                                                                         self.var_dob.get(),
                                                                                                         self.var_email.get(),
                                                                                                         self.var_phone.get(),
                                                                                                         self.var_address.get(),
                                                                                                         self.var_teacher.get(),
                                                                                                         self.var_radio1.get(),
                                                                                                         self.var_std_id.get()

                                                                                                        ))
                    conn.commit()
                else:
                   if not Update:
                       return
                messagebox.showinfo("Success","student Details Successfully Update Completed",parent=self.root)
                self.fetch_data()
                conn.close()

            except Exception as es:
                 messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def delete_data(self):
        if self.var_std_id.get() == "":
          messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student?", parent=self.root)
                if delete:
                  conn = pymysql.connect(host="localhost", user="root", password="root", database="online_student_attendance")
                  my_cursor = conn.cursor()

                  sql = "DELETE FROM student WHERE student_id = %s"
                  val = (self.var_std_id.get(),)

                  my_cursor.execute(sql, val)
                else:
                    if not delete:
                      return
            
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
                
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    def generate_dataset(self):
      if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
        messagebox.showerror("Error", "All Fields are required", parent=self.root)
      else:
        try:
            conn = pymysql.connect(host="localhost", user="root", password="root", database="online_student_attendance")
            my_cursor = conn.cursor()

            my_cursor.execute("SELECT * FROM student")
            myresult = my_cursor.fetchall()
            id = len(myresult) + 1

            # Update student info
            my_cursor.execute("""
                UPDATE student 
                SET Dep=%s, course=%s, Year=%s, Semester=%s, name=%s, Division=%s, Roll=%s,
                    Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s 
                WHERE Student_id=%s
            """, (
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_std_name.get(),
                self.var_div.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var_radio1.get(),
                self.var_std_id.get()
            ))
            conn.commit()
            self.fetch_data()
            # self.reset_data()
            conn.close()

            # ----------- Image Capture -----------
            face_classifier = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    return img[y:y + h, x:x + w]
                return None

            cap = cv2.VideoCapture(0)
            std_id = self.var_std_id.get() 
            img_id = 0
            while True:
                ret, my_frame = cap.read()
                if not ret:
                    break

                cropped_face = face_cropped(my_frame)
                if cropped_face is not None:
                    img_id += 1
                    face_img = cv2.resize(cropped_face, (450, 450))
                    face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
                    
                    import os
                    os.makedirs("data", exist_ok=True)
                
                    file_name_path = f"data/user.{std_id}.jpg"
                    
                    print(file_name_path)
                    cv2.imwrite(file_name_path, face_img)


                    cv2.putText(face_img, str(img_id), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    cv2.imshow("Cropped Face", face_img)

                if cv2.waitKey(1) == 13 or img_id == 100:
                    break

            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Generating data sets completed!!!!")

        except Exception as es:
            messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
