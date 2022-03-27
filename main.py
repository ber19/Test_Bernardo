from src.process import master
from src.variables import globales as varg

def main():
    try:
        varg.ventana = master.Window()
        varg.ventana.start_parent()
    except:
        pass


if __name__ == "__main__":
    main()