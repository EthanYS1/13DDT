from tkinter import *
from PIL import Image, ImageTk
import func as func
import page1 as page1
import pymysql


root = Tk()
root.title("Foodie")
root.geometry("500x800")
root.minsize("500","800")
root.maxsize("500","800")   



#Background gradient as an image
BG_image= Image.open("Images\Login_background.png")
Resized_BG_image = BG_image.resize((1000,1000))
BG=ImageTk.PhotoImage(Resized_BG_image, (1000,1000)) 

#Background gradient place
BGLabel=Label(root, image=BG)
BGLabel.place(x=-300, y=0)

#Entry boxes for username and password
func.user_input_entry = func.user_input(root,370)#Username
func.password_input_entry = func.password_input(root,470)#Password

#Login and sign up buttons
func.Login_button(root,600,func.user_input_entry,func.password_input_entry)
func.signup_button(root)

root.mainloop() 