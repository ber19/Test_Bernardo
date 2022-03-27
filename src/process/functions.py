from src.process.worker import Worker
from src.variables import globales as varg
import asyncio
import threading
import os

def on_closing(ventana):
    for name, elem in ventana.children.items():
        if "worker" in name: 
            elem.count = 0
            elem.alive = False
            elem.destroy()
    os._exit(1)
    


def set_worker(ventana):
    if len(varg.workers) >= 4:
        varg.stack += 1
        ventana.waiting_worker.config(text="{} workers en espera".format(varg.stack))
        ventana.waiting_worker.place(x=50, y=80)
        ventana.rls_workers_btn.place(x=30, y=10)

    varg.limit += 1
    if varg.limit < 2 :
        t = threading.Thread(target=aux2, args=(ventana,))
        t.start()
    else:
        pass
def aux2(ventana):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(aux1(ventana))
    loop.close()
async def aux1(ventana):
    if varg.stack == 0:
        if len(varg.workers) <= 4:
            varg.limit = 0
        worker = Worker(root=ventana, w_number=varg.worker_counter)
        varg.workers[varg.worker_counter] = worker
        varg.worker_counter += 1
        ventana.waiting_worker.place_forget()
        worker.start() 
    else:
        while varg.stack > 0:
            await wait_for_space()
            if varg.stack == 0:
                ventana.waiting_worker.place_forget()
                ventana.rls_workers_btn.place_forget()
                varg.limit = 0
                return
            varg.stack -= 1
            if varg.stack > 0:
                ventana.waiting_worker.config(text="{} workers en espera".format(varg.stack))
                ventana.waiting_worker.place(x=50, y=80)
            if len(varg.workers) <= 4:
                varg.limit = 0
            worker = Worker(root=ventana, w_number=varg.worker_counter)
            varg.workers[varg.worker_counter] = worker
            varg.worker_counter += 1
            if not varg.stack > 0:
                ventana.waiting_worker.place_forget()
                ventana.rls_workers_btn.place_forget()
            worker.start() 



async def wait_for_space():
    while len(varg.workers) >= 4:
        if varg.stack == 0: return
        await asyncio.sleep(.5)


###############################################################

def on_closing_w(ventana):
    ventana.counter_par.destroy()
    ventana.alive = False
    ventana.destroy()
    del varg.workers[ventana.w_number]

def pse_rsm_count(ventana):
    if not ventana.flag1: 
        ventana.flag1 = True
        return
    if ventana.flag1: 
        ventana.flag1 = False
        return

###############################################################


def rerun_workers():
    for worker in varg.workers.values(): 
        worker.ended = False
        worker.count = 0

def release_workers():
    varg.stack = 0



  