import os
import csv
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk

# Global data storage for attendance records
mydata = []

class Attendance:
    """Attendance Management System GUI using Tkinter."""

    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x660+0+0")
        self.root.title("Face Recognition System")

        # Variables for form fields
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # --- UI Setup ---
        self.setup_images()
        self.setup_main_frame()

    def setup_images(self):
        """Load and place header and background images."""
        # Header images
        img1 = Image.open(r"photos\grp stud.jpg").resize((800, 200), Image.Resampling.LANCZOS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        Label(self.root, image=self.photoImg1).place(x=0, y=0, width=800, height=200)

        img2 = Image.open(r"photos\grp sd.jpg").resize((800, 200), Image.Resampling.LANCZOS)
        self.photoImg2 = ImageTk.PhotoImage(img2)
        Label(self.root, image=self.photoImg2).place(x=800, y=0, width=800, height=200)

        # Background image
        img_bg = Image.open(r"photos\cs.jpg").resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoImg_bg = ImageTk.PhotoImage(img_bg)
        Label(self.root, image=self.photoImg_bg).place(x=0, y=200, width=1530, height=710)

    def setup_main_frame(self):
        """Create main frame and all widgets."""
        bg_img = self.root.winfo_children()[-1]  # Last placed widget is bg_img

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1480, height=600)

        # Left frame for form
        self.setup_left_frame(main_frame)
        # Right frame for table
        self.setup_right_frame(main_frame)

    def setup_left_frame(self, parent):
        """Create the left frame with form inputs and buttons."""
        left_frame = LabelFrame(parent, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 15, "bold"))
        left_frame.place(x=10, y=10, width=730, height=580)

        img = Image.open(r"photos\ass.jpg").resize((720, 130), Image.Resampling.LANCZOS)
        self.photoImg_left = ImageTk.PhotoImage(img)
        Label(left_frame, image=self.photoImg_left).place(x=5, y=0, width=720, height=130)

        form_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        form_frame.place(x=0, y=135, width=720, height=370)

        # --- Form fields ---
        Label(form_frame, text="AttendanceId:", font=("times new roman", 13, "bold"), bg="White").grid(row=0, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(form_frame, width=20, textvariable=self.var_atten_id, font=("times new roman", 13, "bold")).grid(row=0, column=1, padx=10, pady=5, sticky=W)

        Label(form_frame, text="Roll:", font=("comicsansns", 11, "bold"), bg="White").grid(row=0, column=2, padx=4, pady=8)
        ttk.Entry(form_frame, width=22, textvariable=self.var_atten_roll, font=("comicsansns", 11, "bold")).grid(row=0, column=3, pady=8)

        Label(form_frame, text="Name:", font=("comicsansns", 11, "bold"), bg="White").grid(row=1, column=0)
        ttk.Entry(form_frame, width=22, textvariable=self.var_atten_name, font=("comicsansns", 11, "bold")).grid(row=1, column=1, pady=8)

        Label(form_frame, text="Department:", font=("comicsansns", 11, "bold"), bg="White").grid(row=1, column=2)
        ttk.Entry(form_frame, width=22, textvariable=self.var_atten_dep, font=("comicsansns", 11, "bold")).grid(row=1, column=3, pady=8)

        Label(form_frame, text="Time:", font=("comicsansns", 11, "bold"), bg="White").grid(row=2, column=0)
        ttk.Entry(form_frame, width=22, textvariable=self.var_atten_time, font=("comicsansns", 11, "bold")).grid(row=2, column=1, pady=8)

        Label(form_frame, text="Date:", font=("comicsansns", 11, "bold"), bg="White").grid(row=2, column=2)
        ttk.Entry(form_frame, width=22, textvariable=self.var_atten_date, font=("comicsansns", 11, "bold")).grid(row=2, column=3, pady=8)

        Label(form_frame, text="Attendance Status:", font=("comicsansns", 11, "bold"), bg="White").grid(row=3, column=0)
        self.atten_status = ttk.Combobox(form_frame, width=20, textvariable=self.var_atten_attendance, font=("comicsansns", 11, "bold"), state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3, column=1, pady=8)

        # --- Buttons ---
        btn_frame = Frame(form_frame, bd=2, relief=RIDGE, bg="WHITE")
        btn_frame.place(x=0, y=300, width=715, height=70)

        Button(btn_frame, text="Import CSV", command=self.importCsv, width=15, font=("times new roman", 13, "bold"), bg="blue", fg="White").grid(row=0, column=0)
        Button(btn_frame, text="Export CSV", command=self.exportCsv, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="White").grid(row=0, column=1)
        Button(btn_frame, text="Update", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="White").grid(row=0, column=2)
        Button(btn_frame, text="Reset", command=self.reset_data, width=20, font=("times new roman", 13, "bold"), bg="blue", fg="White").grid(row=0, column=3)

    def setup_right_frame(self, parent):
        """Create the right frame with the attendance table."""
        right_frame = LabelFrame(parent, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 15, "bold"))
        right_frame.place(x=750, y=10, width=720, height=580)

        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="WHITE")
        table_frame.place(x=5, y=5, width=700, height=455)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(
            table_frame,
            columns=("id", "roll", "name", "department", "time", "date", "attendance"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        for col, text in zip(
            ("id", "roll", "name", "department", "time", "date", "attendance"),
            ("Attendance ID", "Roll", "Name", "Department", "Time", "Date", "Attendance")
        ):
            self.AttendanceReportTable.heading(col, text=text)
            self.AttendanceReportTable.column(col, width=100)

        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    # --- Data Handling Methods ---

    def fetchData(self, rows):
        """Display rows in the attendance table."""
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for row in rows:
            self.AttendanceReportTable.insert("", END, values=row)

    def importCsv(self):
        """Import attendance data from a CSV file."""
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
            parent=self.root
        )
        if fln:
            with open(fln) as myfile:
                csvread = csv.reader(myfile, delimiter=",")
                for row in csvread:
                    mydata.append(row)
            self.fetchData(mydata)

    def exportCsv(self):
        """Export attendance data to a CSV file."""
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data Found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Save CSV",
                defaultextension=".csv",
                filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
                parent=self.root
            )
            if fln:
                with open(fln, mode="w", newline="") as myfile:
                    exp_write = csv.writer(myfile, delimiter=",")
                    for row in mydata:
                        exp_write.writerow(row)
                messagebox.showinfo("Data Export", f"Your data exported to {os.path.basename(fln)} successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        """Fill form fields with the selected row from the table."""
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content.get('values', [])
        if rows:
            self.var_atten_id.set(rows[0])
            self.var_atten_roll.set(rows[1])
            self.var_atten_name.set(rows[2])
            self.var_atten_dep.set(rows[3])
            self.var_atten_time.set(rows[4])
            self.var_atten_date.set(rows[5])
            self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        """Clear all form fields."""
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

if __name__ == "__main__":
    root = Tk()
    app = Attendance(root)
    root.mainloop()

