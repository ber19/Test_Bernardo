from tkinter import ttk, Toplevel, StringVar
import time
from src.process import functions as f
from functools import partial
from threading import Thread
from src.variables import globales as varg


class Worker(Toplevel, Thread):
    def __init__(self, root, w_number):
        Toplevel.__init__(self, root)
        Thread.__init__(self)
        self.parent = root
        self.w_number = w_number
        self.count = 0
        self.alive = True
        self.counter_par = None
        self.flag1 = True
        self.ended = False

        self.title("Worker No.{}".format(self.w_number))
        self.config(width=300, height=100)
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", partial(f.on_closing_w, self))

    def set_counter_parent(self):
        self.counter_par_var = StringVar()
        self.counter_par = ttk.Label(self.parent, textvariable=self.counter_par_var)
        self.counter_par.pack(pady=10)
        self.counter_par_var.set("Iniciando...")

    def run_count(self):
        try:
            while self.alive:
                while self.count != 20 and not self.ended:
                    if not self.alive: return
                    if self.flag1:
                        self.count += 1
                        time.sleep(.5)
                        self.counter_var.set(self.count)
                        self.counter_par_var.set("Worker No.{}   ->   {}".format(self.w_number, self.count))
                self.ended = True
                print([worker.ended for worker in varg.workers.values()])
                if all([worker.ended for worker in varg.workers.values()]):  
                    f.rerun_workers()
        except RuntimeError:
            pass
    
    

    def run(self):
        self.counter_var = StringVar()
        self.counter = ttk.Label(self, textvariable=self.counter_var)
        self.counter.place(x=70, y=40)
        self.btn_stp_count = ttk.Button(self, text="Pausa \\\nResumen", command=partial(f.pse_rsm_count, self))
        self.btn_stp_count.place(x=150, y=30)
        self.set_counter_parent()
        self.run_count()
        
