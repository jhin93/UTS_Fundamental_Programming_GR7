import tkinter as tkt
from login_view import LoginView

def main():
    root = tkt.Tk()
    LoginView(root)
    root.mainloop()

if __name__ == "__main__":
    main()
