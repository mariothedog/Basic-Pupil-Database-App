import tkinter as tk
import tkinter.messagebox as tkMB
import json
import re

from pages.frame_page import FramePage
import pages.page_main_menu as page_main_menu
import constants


class PageRegister(FramePage):
    def create_widgets(self):
        for i in range(2):
            self.rowconfigure(i, weight=1)
            self.columnconfigure(i, weight=1)

        frame_entry = tk.Frame(self, relief=tk.RIDGE, borderwidth=1)
        frame_entry.grid(columnspan=2, pady=(0, 5), sticky=tk.S)

        label_username = tk.Label(frame_entry, text="Username")
        label_password = tk.Label(frame_entry, text="Password")
        label_password_confirm = tk.Label(frame_entry, text="Confirm Password")
        label_username.grid()
        label_password.grid()
        label_password_confirm.grid()

        self.entry_username = tk.Entry(frame_entry, width=15)
        self.entry_password = tk.Entry(frame_entry, width=15, show="*")
        self.entry_password_confirm = tk.Entry(frame_entry, width=15, show="*")
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)
        self.entry_password_confirm.grid(row=2, column=1)

        button_cancel = tk.Button(
            self, text="Cancel", width=5, command=self.cancel)
        button_register = tk.Button(
            self, text="Register", width=5, command=self.register)
        button_cancel.grid(row=1, column=0, padx=(0, 15), sticky=tk.N+tk.E)
        button_register.grid(row=1, column=1, padx=(15, 0), sticky=tk.N+tk.W)

    def cancel(self):
        self.app.show_page(page_main_menu.PageMainMenu)
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
        self.entry_password_confirm.delete(0, tk.END)

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
            self.entry_password.delete(0, tk.END)
            self.entry_password_confirm.delete(0, tk.END)
            return
        elif not password_confirmed:
            tkMB.showerror("Register", "You must confirm your password!")
            return
        elif password != password_confirmed:
            tkMB.showerror("Register", "Your passwords do not match!")
            self.entry_password.delete(0, tk.END)
            self.entry_password_confirm.delete(0, tk.END)
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

        self.app.account_username = username

        tkMB.showinfo("Register", "Account successfully registered")
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
        self.entry_password_confirm.delete(0, tk.END)

        self.app.show_page(page_main_menu.PageMainMenu)
