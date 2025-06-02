# openpls.py
from tkinter import *
from PIL import Image, ImageTk

def openpls():
    root = Tk()
    root.title("Foodie - Page 2")
    root.geometry("500x800")
    root.minsize("500", "800")
    root.maxsize("500", "800")

    Label(root, text="Welcome to Page 2!", font=("Comfortaa", 24), fg="#440c2c").pack(pady=100)

    # Press 's' to close the second page
    def close_on_s(event):
        if event.char == 's':
            root.destroy()

    root.bind('<Key>', close_on_s)
    root.mainloop()
