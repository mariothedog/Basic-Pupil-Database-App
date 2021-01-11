import tkinter as tk

class Application(tk.Frame):
    def __init__(self, parent=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pack(side="top", fill="both", expand=True)
        self.create_widgets()
        self.frame_main.lift()
    
    def create_widgets(self):
        self.frame_main = tk.Frame()
        self.frame_main.place(in_=self, relwidth=1, relheight=1)

        self.frame_login = tk.Frame()
        self.frame_login.place(in_=self, relwidth=1, relheight=1)

        self.create_main_frame()
        self.create_login_frame()
    
    def create_main_frame(self):
        self.frame_main.rowconfigure(0, weight=1)
        self.frame_main.rowconfigure(1, weight=1)
        self.frame_main.columnconfigure(0, weight=1)

        tk.Label(self.frame_main, text="Pupil Database", font=("TkDefaultFont", 16)).grid(sticky=tk.S)

        frame_entry = tk.Frame(self.frame_main, relief="ridge", borderwidth=1)
        frame_entry.grid(row=1, column=0, pady=(10, 0), sticky=tk.N)

        tk.Button(frame_entry, text="Login", width=6, command=self.frame_login.lift).grid(padx=5, pady=5)
        tk.Button(frame_entry, text="Register", width=6).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(frame_entry, text="Exit", width=6, command=self.parent.destroy).grid(row=1, column=0, columnspan=2, pady=(0, 5))

    def create_login_frame(self):
        self.frame_login.rowconfigure(0, weight=1)
        self.frame_login.rowconfigure(1, weight=1)
        self.frame_login.columnconfigure(0, weight=1)
        self.frame_login.columnconfigure(1, weight=1)

        frame_entry = tk.Frame(self.frame_login, relief="ridge", borderwidth=1)
        frame_entry.grid(row=0, column=0, columnspan=2, pady=(0, 5), sticky=tk.S)

        tk.Label(frame_entry, text="Username").grid()
        self.entry_username = tk.Entry(frame_entry, width=15)
        self.entry_username.grid(row=0, column=1)

        tk.Label(frame_entry, text="Password").grid()
        self.entry_password = tk.Entry(frame_entry, width=15, show="*")
        self.entry_password.grid(row=1, column=1)

        tk.Button(self.frame_login, text="Cancel", width=5, command=self.parent.destroy).grid(row=1, column=0, padx=(0, 5), sticky=tk.N+tk.E)
        tk.Button(self.frame_login, text="Login", width=5, command=self.login).grid(row=1, column=1, padx=(5, 0), sticky=tk.N+tk.W)

    def login(self):
        print("Username:", self.entry_username.get())
        print("Password:", self.entry_password.get())
        print()
