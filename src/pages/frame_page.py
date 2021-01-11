import tkinter as tk


class FramePage(tk.Frame):
    def __init__(self, app, *args, **kwargs):
        tk.Frame.__init__(self, None, *args, **kwargs)
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        raise NotImplementedError

    def on_show(self, **kwargs):
        pass
