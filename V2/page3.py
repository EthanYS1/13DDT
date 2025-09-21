from tkinter import *
from PIL import Image, ImageTk
import func as func
import func2 as func2
from tkinter import messagebox

def open_page3():
    root = Tk()
    root.title("Foodie")
    root.geometry("500x800")
    root.minsize(500, 800)
    root.maxsize(500, 800)
    
    BG = Label(root, bg="#61143a")
    BG.place(x=0, y=0, width=500, height=800)
    
    print(f"Current user: {func.current_user}")
    print(f"Current item: {func.current_item}")
    
    # Write review button
    func2.write_review(root)
    
    # Display reviews section
    func2.display_reviews(root)
    
    def close_on_s(event):
        if event.char == 's':
            root.destroy()

    root.bind('<Key>', close_on_s)
    root.mainloop()