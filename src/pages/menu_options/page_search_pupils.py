import tkinter as tk
import tkinter.messagebox as tkMB
import json

from pages.frame_page import FramePage
import constants
from util.scrolling_listbox import ScrollingListbox
import pages.menu_options.page_option_menu as page_option_menu


class PageSearchPupils(FramePage):
    def create_widgets(self):
        self.rowconfigure(3, weight=1)
        for i in range(3):
            self.columnconfigure(i, weight=1)

        frame_entry = tk.Frame(self, relief=tk.RIDGE, borderwidth=1)
        frame_entry.grid(columnspan=3, pady=10)

        self.search_term = tk.StringVar()
        self.search_term.trace_add("write", self.on_search_term_change)

        label_search_term = tk.Label(frame_entry, text="Search")
        self.entry_search_term = tk.Entry(
            frame_entry, textvariable=self.search_term)
        label_search_term.grid()
        self.entry_search_term.grid(row=0, column=1)

        frame_buttons = tk.Frame(self)
        frame_buttons.grid(columnspan=3, pady=(0, 20))

        button_cancel = tk.Button(
            frame_buttons, text="Cancel", command=self.cancel)
        button_cancel.grid(padx=(0, 5), sticky=tk.E)

        label_header_pupils = tk.Label(
            self, text="Pupils", font=("TkDefaultFont", 14))
        label_header_pupils.grid(row=2, column=1, sticky=tk.S)

        self.frame_pupils = ScrollingListbox(self)
        self.frame_pupils.grid(row=3, column=1, sticky=tk.N)

    def on_show(self):
        with open(constants.JSON_ACCOUNTS, "a+") as file:
            file.seek(0)
            account_json_data = file.read()
        account_data = json.loads(account_json_data)
        current_account_data = account_data[self.app.account_username]
        pupils = current_account_data["pupils"]

        self.frame_pupils.list_variable.set(pupils)

    def on_search_term_change(self, *args):
        search_term = self.search_term.get()

        with open(constants.JSON_ACCOUNTS, "a+") as file:
            file.seek(0)
            account_json_data = file.read()
        account_data = json.loads(account_json_data)
        current_account_data = account_data[self.app.account_username]
        pupils = current_account_data["pupils"]

        filtered_pupils = [p for p in pupils if p.startswith(search_term)]

        self.frame_pupils.list_variable.set(filtered_pupils)

    def cancel(self):
        self.app.show_page(page_option_menu.PageOptionMenu)
        self.entry_search_term.delete(0, tk.END)
