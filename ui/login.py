import tkinter as tk
from tkinter import messagebox

# Import main app
from ui.main_app import StudentApp


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Login - Student Management System")
        self.root.geometry("420x300")
        self.root.configure(bg="#ecf0f1")
        self.root.resizable(False, False)

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.create_ui()

    def create_ui(self):
        title = tk.Label(
            self.root,
            text="🎓 Admin Login",
            font=("Segoe UI", 20, "bold"),
            bg="#2c3e50",
            fg="white",
            pady=10
        )
        title.pack(fill=tk.X)

        login_frame = tk.Frame(self.root, bg="white", bd=2, relief=tk.RIDGE)
        login_frame.place(x=55, y=75, width=310, height=180)

        tk.Label(login_frame, text="👤 Username",
                 font=("Segoe UI", 11, "bold"),
                 bg="white", fg="#2c3e50").place(x=20, y=25)

        tk.Entry(login_frame, textvariable=self.username,
                 font=("Segoe UI", 10), width=20).place(x=130, y=25)

        tk.Label(login_frame, text="🔑 Password",
                 font=("Segoe UI", 11, "bold"),
                 bg="white", fg="#2c3e50").place(x=20, y=70)

        tk.Entry(login_frame, textvariable=self.password,
                 font=("Segoe UI", 10), width=20, show="*").place(x=130, y=70)

        tk.Button(
            login_frame,
            text="🔓 Login",
            command=self.check_login,
            bg="#3498db",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            relief=tk.FLAT,
            width=15,
            cursor="hand2"
        ).place(x=85, y=120)

    def check_login(self):
        username = self.username.get().strip()
        password = self.password.get().strip()

        # Simple authentication (can be improved later)
        if username == "admin" and password == "1234":
            messagebox.showinfo("Login Success", "Welcome Admin!")

            # Close login window
            self.root.destroy()

            # Open main app
            main_root = tk.Tk()
            app = StudentApp(main_root)
            main_root.mainloop()

        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
