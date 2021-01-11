import tkinter as tk

from pages.frame_page import FramePage
from pages.menu_options.page_add_pupil import PageAddPupil
from pages.menu_options.page_amend_pupil import PageAmendPupil
from pages.menu_options.page_search_pupils import PageSearchPupils


class PageOptionMenu(FramePage):
    def create_widgets(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(4, weight=1)
        self.columnconfigure(0, weight=1)

        BUTTON_WIDTH = 10
        tk.Button(self, text="Add Pupil", width=BUTTON_WIDTH,
                  command=lambda: self.app.show_page(PageAddPupil)).grid(sticky=tk.S)
        tk.Button(self, text="Amend Pupil", width=BUTTON_WIDTH,
                  command=lambda: self.app.show_page(PageAmendPupil)).grid()
        tk.Button(self, text="Search Pupils", width=BUTTON_WIDTH, command=lambda: self.app.show_page(PageSearchPupils)).grid()
        tk.Button(self, text="Quiz", width=BUTTON_WIDTH).grid()
        tk.Button(self, text="Log Out", width=BUTTON_WIDTH,
                  command=self.app.log_out).grid(sticky=tk.N)
