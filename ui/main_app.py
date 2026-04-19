import tkinter as tk
from tkinter import ttk, messagebox

from data.database import connect_db
from services.student_service import *


class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎓 Student Management System")
        self.root.geometry("1280x700")
        self.root.configure(bg="#ecf0f1")

        connect_db()

        # Variables
        self.roll = tk.StringVar()
        self.name = tk.StringVar()
        self.cls = tk.StringVar()
        self.section = tk.StringVar()
        self.contact = tk.StringVar()
        self.father = tk.StringVar()
        self.gender = tk.StringVar()
        self.dob = tk.StringVar()
        self.search_by = tk.StringVar(value="roll")
        self.search_txt = tk.StringVar()

        self.create_ui()
        self.show_all()

    # ---------------- UI ----------------
    def create_ui(self):
        title = tk.Label(self.root, text="🎓 Student Management System",
                         font=("Segoe UI", 22, "bold"),
                         bg="#2c3e50", fg="white", pady=8)
        title.pack(fill=tk.X)

        main_frame = tk.Frame(self.root, bg="#ecf0f1")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

        # LEFT FORM
        form = tk.LabelFrame(main_frame, text="Student Details",
                             font=("Segoe UI", 12, "bold"),
                             bg="white")
        form.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        fields = [
            ("Roll", self.roll),
            ("Name", self.name),
            ("Class", self.cls),
            ("Section", self.section),
            ("Contact", self.contact),
            ("Father", self.father),
            ("DOB", self.dob)
        ]

        for i, (label, var) in enumerate(fields):
            tk.Label(form, text=label, bg="white").grid(row=i, column=0, padx=5, pady=5)
            tk.Entry(form, textvariable=var).grid(row=i, column=1, padx=5, pady=5)

        ttk.Combobox(form, textvariable=self.gender,
                     values=["Male", "Female", "Other"],
                     state="readonly").grid(row=7, column=1)

        self.address = tk.Text(form, height=3, width=25)
        self.address.grid(row=8, column=1)

        # Buttons
        btns = tk.Frame(form, bg="white")
        btns.grid(row=9, columnspan=2)

        tk.Button(btns, text="Add", command=self.add_student).grid(row=0, column=0)
        tk.Button(btns, text="Update", command=self.update_student).grid(row=0, column=1)
        tk.Button(btns, text="Delete", command=self.delete_student).grid(row=1, column=0)
        tk.Button(btns, text="Clear", command=self.clear).grid(row=1, column=1)

        # RIGHT TABLE
        table_frame = tk.Frame(main_frame)
        table_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        search_frame = tk.Frame(table_frame)
        search_frame.pack(fill=tk.X)

        ttk.Combobox(search_frame, textvariable=self.search_by,
                     values=["roll", "name", "class", "contact"],
                     state="readonly").pack(side=tk.LEFT)

        tk.Entry(search_frame, textvariable=self.search_txt).pack(side=tk.LEFT)

        tk.Button(search_frame, text="Search", command=self.search).pack(side=tk.LEFT)
        tk.Button(search_frame, text="Show All", command=self.show_all).pack(side=tk.LEFT)

        columns = ("roll", "name", "class", "section", "contact", "father", "address", "gender", "dob")

        self.table = ttk.Treeview(table_frame, columns=columns, show="headings")

        for col in columns:
            self.table.heading(col, text=col)

        self.table.pack(fill=tk.BOTH, expand=True)
        self.table.bind("<ButtonRelease-1>", self.get_data)

    # ---------------- FUNCTIONS ----------------
    def add_student(self):
        try:
            add_student((
                self.roll.get(),
                self.name.get(),
                self.cls.get(),
                self.section.get(),
                self.contact.get(),
                self.father.get(),
                self.address.get("1.0", tk.END),
                self.gender.get(),
                self.dob.get()
            ))
            messagebox.showinfo("Success", "Student Added")
            self.show_all()
            self.clear()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_all(self):
        rows = get_all_students()
        self.table.delete(*self.table.get_children())
        for row in rows:
            self.table.insert("", tk.END, values=row)

    def get_data(self, ev):
        row = self.table.item(self.table.focus())["values"]
        if row:
            self.roll.set(row[0])
            self.name.set(row[1])
            self.cls.set(row[2])
            self.section.set(row[3])
            self.contact.set(row[4])
            self.father.set(row[5])
            self.gender.set(row[7])
            self.dob.set(row[8])

            self.address.delete("1.0", tk.END)
            self.address.insert(tk.END, row[6])

    def update_student(self):
        update_student((
            self.name.get(),
            self.cls.get(),
            self.section.get(),
            self.contact.get(),
            self.father.get(),
            self.address.get("1.0", tk.END),
            self.gender.get(),
            self.dob.get(),
            self.roll.get()
        ))
        messagebox.showinfo("Updated", "Record Updated")
        self.show_all()

    def delete_student(self):
        delete_student(self.roll.get())
        messagebox.showinfo("Deleted", "Record Deleted")
        self.show_all()
        self.clear()

    def clear(self):
        self.roll.set("")
        self.name.set("")
        self.cls.set("")
        self.section.set("")
        self.contact.set("")
        self.father.set("")
        self.gender.set("")
        self.dob.set("")
        self.address.delete("1.0", tk.END)

    def search(self):
        rows = search_students(self.search_by.get(), self.search_txt.get())
        self.table.delete(*self.table.get_children())
        for row in rows:
            self.table.insert("", tk.END, values=row)
