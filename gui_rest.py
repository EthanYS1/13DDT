from tkinter import *
from PIL import Image, ImageTk

def openpls():
    root = Tk()
    root.title("Foodie")
    root.geometry("500x800")
    root.minsize("500","800")
    root.maxsize("500","800")


        
    def close_on_s(event):
        if event.char == 's':
            root.destroy()

    root.bind('<Key>', close_on_s)
    root.mainloop()
    
