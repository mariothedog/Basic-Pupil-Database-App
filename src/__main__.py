import tkinter as tk
from application import Application

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("250x250")
    root.title("Pupil Database")
    app = Application(parent=root, highlightbackground="black",
                      highlightthickness=3)
    app.mainloop()
