from tkinter import *
from PIL import Image, ImageTk
import func 

root = Tk()
root.title("Foodie")
root.geometry("500x800")
root.minsize("500","800")
root.maxsize("500","800")

BG_image= Image.open("Ethan_13DDT_/Images/LGBG.png")
Resized_BG_image= BG_image.resize((1000,1000))
BG=ImageTk.PhotoImage(Resized_BG_image) 
def B1():
    BGLabel=Label( image=BG)
    BGLabel.place(x=-300, y=0)

B1()

func.Logo(root,50)

func.Login_input(root,370)#Username
func.Login_input(root,470)#Password

func.Login_button(root,600)

root.mainloop()