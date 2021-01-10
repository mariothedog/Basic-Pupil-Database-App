import tkinter as tk
from application import Application

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pupil Database")
    app = Application(parent=root)
    app.mainloop()
