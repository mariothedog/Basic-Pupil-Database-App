import tkinter as tk
from frame_page import FramePage
import frame_main_menu as mm

class FrameRegister(FramePage):
    def create_widgets(self):
        for i in range(2):
            self.rowconfigure(i, weight=1)
            self.columnconfigure(i, weight=1)

        frame_entry = tk.Frame(self, relief="ridge", borderwidth=1)
        frame_entry.grid(columnspan=2, pady=(0, 5), sticky=tk.S)

        tk.Label(frame_entry, text="Username").grid()
        self.entry_username = tk.Entry(frame_entry, width=15)
        self.entry_username.grid(row=0, column=1)

        tk.Label(frame_entry, text="Password").grid()
        self.entry_password = tk.Entry(frame_entry, width=15, show="*")
        self.entry_password.grid(row=1, column=1)

        tk.Label(frame_entry, text="Confirm Password").grid()
        self.entry_password_confirm = tk.Entry(frame_entry, width=15, show="*")
        self.entry_password_confirm.grid(row=2, column=1)

        tk.Button(self, text="Cancel", width=5, command=lambda: self.app.show_frame(mm.FrameMainMenu)).grid(row=1, column=0, padx=(0, 15), sticky=tk.N+tk.E)
        tk.Button(self, text="Register", width=5, command=self.register).grid(row=1, column=1, padx=(15, 0), sticky=tk.N+tk.W)
    
    def register(self):
        print("Username:", self.entry_username.get())
        print("Password:", self.entry_password.get())
        print("Re-entered Password:", self.entry_password_confirm.get())
        print()