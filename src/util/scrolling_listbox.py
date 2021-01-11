import tkinter as tk


class ScrollingListbox(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.list_variable = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        listbox = tk.Listbox(self, yscrollcommand=scrollbar.set,
                                  listvariable=self.list_variable, bg="SystemButtonFace")
        listbox.pack()

        scrollbar.config(command=listbox.yview)
