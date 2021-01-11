import tkinter as tk
from frame_page import FramePage
import frame_login
import frame_register


class FrameMainMenu(FramePage):
    def create_widgets(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        tk.Label(self, text="Pupil Database", font=(
            "TkDefaultFont", 16)).grid(sticky=tk.S)

        frame_entry = tk.Frame(self, relief=tk.RIDGE, borderwidth=1)
        frame_entry.grid(row=1, column=0, pady=(10, 0), sticky=tk.N)

        tk.Button(frame_entry, text="Login", width=6, command=lambda: self.app.show_frame(
            frame_login.FrameLogin)).grid(padx=5, pady=5)
        tk.Button(frame_entry, text="Register", width=6, command=lambda: self.app.show_frame(
            frame_register.FrameRegister)).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(frame_entry, text="Exit", width=6, command=self.app.parent.destroy).grid(
            row=1, column=0, columnspan=2, pady=(0, 5))
