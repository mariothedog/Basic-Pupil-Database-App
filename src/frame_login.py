import tkinter as tk
import tkinter.messagebox as tkMB
import json

from frame_page import FramePage
import constants
import frame_main_menu
import menu_options.frame_option_menu as frame_option_menu


class FrameLogin(FramePage):
    def create_widgets(self):
        for i in range(2):
            self.rowconfigure(i, weight=1)
            self.columnconfigure(i, weight=1)

        frame_entry = tk.Frame(self, relief=tk.RIDGE, borderwidth=1)
        frame_entry.grid(columnspan=2, pady=(0, 5), sticky=tk.S)

        label_username = tk.Label(frame_entry, text="Username")
        label_password = tk.Label(frame_entry, text="Password")
        label_username.grid()
        label_password.grid()

        self.entry_username = tk.Entry(frame_entry, width=15)
        self.entry_password = tk.Entry(frame_entry, width=15, show="*")
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        button_cancel = tk.Button(self, text="Cancel", width=5, command=lambda: self.app.show_frame(
            frame_main_menu.FrameMainMenu))
        button_login = tk.Button(
            self, text="Login", width=5, command=self.login)
        button_cancel.grid(row=1, column=0, padx=(0, 5), sticky=tk.N+tk.E)
        button_login.grid(row=1, column=1, padx=(5, 0), sticky=tk.N+tk.W)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if not username:
            tkMB.showerror("Register", "You must enter a username!")
            return
        elif not password:
            tkMB.showerror("Register", "You must enter a password!")
            return

        with open(constants.JSON_ACCOUNTS, "a+") as file:
            file.seek(0)
            account_json_data = file.read()
        try:
            account_data = json.loads(account_json_data)
        except json.decoder.JSONDecodeError:
            account_data = {}

        if username not in account_data:
            tkMB.showerror("Login", "Username not recognised!\n"
                                    "Remember to register first if you have "
                                    "not done so already.")
            return

        account = account_data[username]
        if password != account["password"]:
            tkMB.showerror("Login", "Incorrect password!")
            self.entry_password.delete(0, tk.END)
            return

        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

        self.app.account_username = username

        self.app.show_frame(frame_option_menu.FrameOptionMenu)
