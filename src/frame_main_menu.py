import tkinter as tk
from frame_page import FramePage
import frame_login
import frame_register


class FrameMainMenu(FramePage):
    def create_widgets(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        label_header = tk.Label(
            self, text="Pupil Database", font=("TkDefaultFont", 16))
        label_header.grid(sticky=tk.S)

        frame_entry = tk.Frame(self, relief=tk.RIDGE, borderwidth=1)
        frame_entry.grid(row=1, column=0, pady=(10, 0), sticky=tk.N)

        button_login = tk.Button(frame_entry, text="Login", width=6,
                                 command=lambda: self.app.show_frame(frame_login.FrameLogin))
        button_register = tk.Button(frame_entry, text="Register", width=6,
                                    command=lambda: self.app.show_frame(frame_register.FrameRegister))
        button_exit = tk.Button(frame_entry, text="Exit",
                                width=6, command=self.app.parent.destroy)
        button_login.grid(padx=5, pady=5)
        button_register.grid(row=0, column=1, padx=5, pady=5)
        button_exit.grid(row=1, column=0, columnspan=2, pady=(0, 5))
