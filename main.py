from tkinter import *
from PIL import Image, ImageTk
import func as func
import page1 as page1


root = Tk()
root.title("Foodie")
root.geometry("500x800")
root.minsize("500","800")
root.maxsize("500","800")   

# func.B1(root)

BG_image= Image.open("Images\Login_background.png")
Resized_BG_image = BG_image.resize((1000,1000))
BG=ImageTk.PhotoImage(Resized_BG_image, (1000,1000)) 

BGLabel=Label(root, image=BG)
BGLabel.place(x=-300, y=0)

user_entry = func.user_input(root,370)#Username
password_entry = func.password_input(root,470)#Password
func.Login_success
func.Login_button(root,600,user_entry,password_entry)

root.mainloop()