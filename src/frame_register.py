import tkinter as tk
import tkinter.messagebox as tkMB
import json
import re

from frame_page import FramePage
import frame_main_menu
import constants


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

        tk.Button(self, text="Cancel", width=5, command=lambda: self.app.show_frame(
            frame_main_menu.FrameMainMenu)).grid(row=1, column=0, padx=(0, 15), sticky=tk.N+tk.E)
        tk.Button(self, text="Register", width=5, command=self.register).grid(
            row=1, column=1, padx=(15, 0), sticky=tk.N+tk.W)

    def register(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        password_confirmed = self.entry_password_confirm.get()

        if not username:
            tkMB.showerror("Register", "You must enter a username!")
            return
        elif not password:
            tkMB.showerror("Register", "You must enter a password!")
            return
        elif not re.match(constants.RE_PASSWORD, password):
            tkMB.showerror("Register", ("Your password must meet the following criteria:\n"
                                        "- Minimum length of 8 characters\n"
                                        "- At least one uppercase letter\n"
                                        "- At least one number"))
            self.entry_password.delete(0, "end")
            self.entry_password_confirm.delete(0, "end")
            return
        elif not password_confirmed:
            tkMB.showerror("Register", "You must confirm your password!")
            return
        elif password != password_confirmed:
            tkMB.showerror("Register", "Your passwords do not match!")
            self.entry_password.delete(0, "end")
            self.entry_password_confirm.delete(0, "end")
            return

        with open(constants.JSON_ACCOUNTS, "a+") as file:
            file.seek(0)
            account_json_data = file.read()
        try:
            account_data = json.loads(account_json_data)
        except json.decoder.JSONDecodeError:
            account_data = {}

        account_data[self.entry_username.get()] = {
            "password": self.entry_password.get(),
            "pupils": []
        }
        with open("accounts.json", "w") as file:
            file.write(json.dumps(account_data, indent=4))

        tkMB.showinfo("Register", "Account successfully registered")
        self.entry_username.delete(0, "end")
        self.entry_password.delete(0, "end")
        self.entry_password_confirm.delete(0, "end")

        self.app.show_frame(frame_main_menu.FrameMainMenu)
