import tkinter as tk
from frame_main_menu import FrameMainMenu
from frame_login import FrameLogin
from frame_register import FrameRegister
from frame_option_menu import FrameOptionMenu


class Application(tk.Frame):
    def __init__(self, parent=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pack(side="top", fill="both", expand=True)
        self.frames = self.create_frames()
        self.account = None
        self.show_frame(FrameMainMenu)

    def create_frames(self):
        frames = {}
        for frame in {FrameMainMenu, FrameLogin, FrameRegister, FrameOptionMenu}:
            f = frame(self)
            f.place(in_=self, relwidth=1, relheight=1)
            frames[frame] = f
        return frames

    def show_frame(self, frame_page):
        self.frames[frame_page].lift()
