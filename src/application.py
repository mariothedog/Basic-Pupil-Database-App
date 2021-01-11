import tkinter as tk

from frame_main_menu import FrameMainMenu
from frame_login import FrameLogin
from frame_register import FrameRegister
from menu_options.frame_option_menu import FrameOptionMenu
from menu_options.frame_add_pupil import FrameAddPupil


class Application(tk.Frame):
    def __init__(self, parent=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.account_username = ""
        self.frames = self.create_frames()
        self.show_frame(FrameMainMenu)

    def create_frames(self):
        frames = {}
        for frame in {FrameMainMenu, FrameLogin, FrameRegister,
                      FrameOptionMenu, FrameAddPupil}:
            f = frame(self)
            f.place(in_=self, relwidth=1, relheight=1)
            frames[frame] = f
        return frames

    def show_frame(self, frame_page):
        frame = self.frames[frame_page]
        frame.on_show()
        frame.lift()

    def log_out(self):
        self.account_username = ""
        self.show_frame(FrameMainMenu)
