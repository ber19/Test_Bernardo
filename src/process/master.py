from tkinter import ttk, Tk
from functools import partial
from src.process import functions as f

class Window(Tk):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

        self.title("Master")
        self.config(width=300, height=300)
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", partial(f.on_closing, self))

        self.set_worker_btn = ttk.Button(
            self, text="Worker", width=20,
            command=partial(f.set_worker, self)
            )
        self.set_worker_btn.pack(padx=50, pady=40)

        self.rls_workers_btn = ttk.Button(
            self, text="Liberar stack",
            command=f.release_workers
        )
        # self.rls_workers_btn.place(x=30,y=10)

        self.waiting_worker = ttk.Label(self)


    def start_parent(self):
        self.mainloop()