# import tkinter as tkt
# from login_view import LoginView

# Add the parent directory to Python path
import sys
import os
import tkinter as tkt

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gui.views.login_view import LoginView

def main():
    root = tkt.Tk()
    LoginView(root)
    root.mainloop()

if __name__ == "__main__":
    main()
