from src.process import master
from src.variables import globales as varg
import os

def main():
    try:
        varg.ventana = master.Window()
        varg.ventana.start_parent()
    except:
        os.__exit(1)


if __name__ == "__main__":
    main()