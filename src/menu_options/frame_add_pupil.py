import tkinter as tk
import tkinter.messagebox as tkMB
import json

from frame_page import FramePage
import constants
from util.scrolling_listbox import ScrollingListbox
import menu_options.frame_option_menu as frame_option_menu


class FrameAddPupil(FramePage):
    def create_widgets(self):
        self.rowconfigure(3, weight=1)
        for i in range(3):
            self.columnconfigure(i, weight=1)

        frame_entry = tk.Frame(self, relief="ridge", borderwidth=1)
        frame_entry.grid(columnspan=3, pady=10)

        tk.Label(frame_entry, text="Pupil Name").grid()
        self.entry_pupil_name = tk.Entry(frame_entry, text="Pupil Name")
        self.entry_pupil_name.grid(row=0, column=1)

        frame_buttons = tk.Frame(self)
        frame_buttons.grid(columnspan=3, pady=(0, 20))

        tk.Button(frame_buttons, text="Cancel", command=lambda: self.app.show_frame(
            frame_option_menu.FrameOptionMenu)).grid(padx=(0, 5), sticky=tk.E)
        tk.Button(frame_buttons, text="Add Pupil", command=self.add_pupil).grid(
            row=0, column=2, padx=(5, 0), sticky=tk.W)

        tk.Label(self, text="Pupils", font=("TkDefaultFont", 14)).grid(
            row=2, column=1, sticky=tk.S)

        self.frame_pupils = ScrollingListbox(self)
        self.frame_pupils.grid(row=3, column=1, sticky=tk.N)

    def add_pupil(self):
        name = self.entry_pupil_name.get()
        if not name:
            tkMB.showerror("Add Pupil", "You must enter a name!")
            return

        with open(constants.JSON_ACCOUNTS, "a+") as file:
            file.seek(0)
            account_json_data = file.read()
        account_data = json.loads(account_json_data)

        pupils = account_data[self.app.account_username]["pupils"]
        pupils.append(name)
        with open("accounts.json", "w") as file:
            file.write(json.dumps(account_data, indent=4))

        tkMB.showinfo("Add Pupil", "Pupil successfully added")
        self.entry_pupil_name.delete(0, tk.END)

        self.frame_pupils.list_variable.set(pupils)
    
    def on_show(self):
        with open(constants.JSON_ACCOUNTS, "a+") as file:
            file.seek(0)
            account_json_data = file.read()
        account_data = json.loads(account_json_data)
        current_account_data = account_data[self.app.account_username]
        pupils = current_account_data["pupils"]

        self.frame_pupils.list_variable.set(pupils)