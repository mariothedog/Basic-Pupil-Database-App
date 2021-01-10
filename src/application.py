import tkinter as tk

class Application(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.pack(expand=True)
        self.create_widgets()
    
    def create_widgets(self):
        self.create_login_widgets()

    def create_login_widgets(self):
        self.frame_login = tk.Frame(self)
        self.frame_login.pack()

        frame_entry = tk.Frame(self.frame_login, relief="ridge", borderwidth=1)
        frame_entry.grid(row=0, column=0, columnspan=2, pady=(0, 5))

        tk.Label(frame_entry, text="Username").grid()
        self.entry_username = tk.Entry(frame_entry, width=15)
        self.entry_username.grid(row=0, column=1)

        tk.Label(frame_entry, text="Password").grid()
        self.entry_password = tk.Entry(frame_entry, width=15, show="*")
        self.entry_password.grid(row=1, column=1)

        tk.Button(self.frame_login, text="Cancel", width=5, command=self.parent.destroy).grid(row=1, column=0)
        tk.Button(self.frame_login, text="Login", width=5, command=self.login).grid(row=1, column=1)

    def login(self):
        print("Username:", self.entry_username.get())
        print("Password:", self.entry_password.get())
        print()
