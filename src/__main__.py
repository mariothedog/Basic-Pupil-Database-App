import tkinter as tk
from application import Application

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("200x200")
    app = Application(parent=root)
    app.mainloop()
