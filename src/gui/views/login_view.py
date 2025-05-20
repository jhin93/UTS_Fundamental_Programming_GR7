import tkinter as tkt
from tkinter import messagebox
from ..controllers.gui_controller import handle_login
from ..views.exception_view import show_exception


class LoginView:
    def __init__(self, window):
        self.window = window
        self.window.title(" main Login Window")

        tkt.Label(window, text="Email id:").pack()
        self.email_entry = tkt.Entry(window)
        self.email_entry.pack()

        tkt.Label(window, text="Password:").pack()
        self.password_entry = tkt.Entry(window, show="*")
        self.password_entry.pack()

        tkt.Button(window, text="Login", command=self.login).pack(pady=10)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        success, message = handle_login(email, password)

        if success:
            messagebox.showinfo("Successfull", message)
        else:
            show_exception(message)
