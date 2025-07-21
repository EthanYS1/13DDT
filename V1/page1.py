from tkinter import *
from PIL import Image, ImageTk
import func as func



def open_page1():
    root = Tk()
    root.title("Foodie")
    root.geometry("500x800")
    root.minsize("500","800")
    root.maxsize("500","800")
    
    BG= Label(root, bg="#61143a")
    BG.place(x=0,y=0,width=500,height=800)
    
    func.listing(root, 50, "Images\Rat.png", "KFC", "rat", "This fried KFC is very good", "$20.00")

    func.listing(root,325, "Images\Turty.png", "Fired Turtle", "turtle", "This turtle tastes good trust", "$50.00")
   
  
    
 
    

                
    def close_on_s(event):
        if event.char == 's':
            root.destroy()

    root.bind('<Key>', close_on_s)
    root.mainloop()

    



