import tkinter as tk

from pages.frame_page import FramePage
from pages.menu_options.page_add_pupil import PageAddPupil
from pages.menu_options.page_amend_pupil import PageAmendPupil
from pages.menu_options.page_search_pupils import PageSearchPupils
from pages.menu_options.page_quiz import PageQuiz


class PageOptionMenu(FramePage):
    def create_widgets(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(4, weight=1)
        self.columnconfigure(0, weight=1)

        BUTTON_WIDTH = 10
        button_add_pupil = tk.Button(
            self, text="Add Pupil", width=BUTTON_WIDTH, command=lambda: self.app.show_page(PageAddPupil))
        button_amend_pupil = tk.Button(
            self, text="Amend Pupil", width=BUTTON_WIDTH, command=lambda: self.app.show_page(PageAmendPupil))
        button_search_pupils = tk.Button(
            self, text="Search Pupils", width=BUTTON_WIDTH, command=lambda: self.app.show_page(PageSearchPupils))
        button_quiz = tk.Button(
            self, text="Quiz", width=BUTTON_WIDTH, command=lambda: self.app.show_page(PageQuiz))
        button_log_out = tk.Button(
            self, text="Log Out", width=BUTTON_WIDTH, command=self.app.log_out)

        button_add_pupil.grid(sticky=tk.S)
        button_amend_pupil.grid()
        button_search_pupils.grid()
        button_quiz.grid()
        button_log_out.grid(sticky=tk.N)
