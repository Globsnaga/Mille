from Reader import FileHandler
from tkinter import filedialog,Tk
import tkinter

if __name__ == '__main__':
    Tk().withdraw()
    r = FileHandler()
    list = r.readFile(filedialog.askopenfilename())


    remover = []



    r.writeFile(filedialog.asksaveasfilename(),list)