import tkinter as tk
import tkinter.messagebox as tkMB
import json

from pages.frame_page import FramePage
import constants
from util.scrolling_listbox import ScrollingListbox
import pages.menu_options.page_option_menu as page_option_menu


class PageAmendPupil(FramePage):
    def create_widgets(self):
        self.rowconfigure(3, weight=1)
        for i in range(3):
            self.columnconfigure(i, weight=1)

        frame_entry = tk.Frame(self, relief=tk.RIDGE, borderwidth=1)
        frame_entry.grid(columnspan=3, pady=10)

        label_id = tk.Label(frame_entry, text="Pupil ID")
        label_new_name = tk.Label(frame_entry, text="New Name")
        label_id.grid()
        label_new_name.grid()

        self.entry_id = tk.Entry(frame_entry)
        self.entry_new_name = tk.Entry(frame_entry)
        self.entry_id.grid(row=0, column=1)
        self.entry_new_name.grid(row=1, column=1)

        frame_buttons = tk.Frame(self)
        frame_buttons.grid(columnspan=3, pady=(0, 20))

        button_cancel = tk.Button(frame_buttons, text="Cancel", command=lambda: self.app.show_page(
            page_option_menu.PageOptionMenu))
        button_amend = tk.Button(
            frame_buttons, text="Amend Pupil", command=self.amend_pupil)
        button_cancel.grid(padx=(0, 5), sticky=tk.E)
        button_amend.grid(row=0, column=2, padx=(5, 0), sticky=tk.W)

        label_header_pupils = tk.Label(
            self, text="Pupils", font=("TkDefaultFont", 14))
        label_header_pupils.grid(row=2, column=1, sticky=tk.S)

        self.frame_pupils = ScrollingListbox(self)
        self.frame_pupils.grid(row=3, column=1, sticky=tk.N)
    
    def update_list(self):
        with open(constants.JSON_ACCOUNTS, "a+") as file:
            file.seek(0)
            account_json_data = file.read()
        account_data = json.loads(account_json_data)
        current_account_data = account_data[self.app.account_username]
        pupils = current_account_data["pupils"]

        pupil_ids = ["%d - %s" % (i + 1, p) for i, p in enumerate(pupils)]
        self.frame_pupils.list_variable.set(pupil_ids)

    def amend_pupil(self):
        id = self.entry_id.get()
        new_name = self.entry_new_name.get()

        if not id:
            tkMB.showerror("Amend Pupil", "You must enter a pupil ID!")
            return
        elif not new_name:
            tkMB.showerror("Amend Pupil", "You must enter a new name!")
            return
        
        id = int(id)
        if id <= 0:
            tkMB.showerror("Amend Pupil", "The pupil ID must be 1 or higher!")
            return
        
        with open(constants.JSON_ACCOUNTS, "a+") as file:
            file.seek(0)
            account_json_data = file.read()
        account_data = json.loads(account_json_data)
        current_account_data = account_data[self.app.account_username]
        pupils = current_account_data["pupils"]

        try:
            pupils[id - 1] = new_name
        except IndexError:
            tkMB.showerror("Amend Pupil", "The pupil ID entered is too high!")
            return

        with open("accounts.json", "w") as file:
            file.write(json.dumps(account_data, indent=4))
        
        self.update_list()

    def on_show(self):
        self.update_list()
