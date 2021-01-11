import tkinter as tk

from page_main_menu import PageMainMenu
from page_login import PageLogin
from page_register import PageRegister
from menu_options.page_option_menu import PageOptionMenu
from menu_options.page_add_pupil import PageAddPupil


class Application(tk.Frame):
    def __init__(self, parent=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.account_username = ""
        self.pages = self.create_pages()
        self.show_page(PageMainMenu)

    def create_pages(self):
        pages = {}
        for page in {PageMainMenu, PageLogin, PageRegister,
                      PageOptionMenu, PageAddPupil}:
            p = page(self)
            p.place(in_=self, relwidth=1, relheight=1)
            pages[page] = p
        return pages

    def show_page(self, frame_page):
        page = self.pages[frame_page]
        page.on_show()
        page.lift()

    def log_out(self):
        self.account_username = ""
        self.show_page(PageMainMenu)
