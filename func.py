from tkinter import *
from PIL import Image, ImageTk


BG_image= Image.open("Ethan_13DDT_/Images/LGBG.png")
Resized_BG_image= BG_image.resize((1000,1000))
BG=ImageTk.PhotoImage(Resized_BG_image) 
def B1():
    BGLabel=Label( image=BG)
    BGLabel.place(x=-300, y=0)

def Login_success(root,):
    root.destroy()
  

def Logo(root,Logo_y):
    BG_image= Image.open("Ethan_13DDT_/Images/LGBG.png")
    Logo=ImageTk.PhotoImage(BG_image) 
    Logo_label=Label(root, image=Logo)
    Logo_label.place (x=125,y=Logo_y,width=250,height=250)

def Login_button(root,Login_button_y):
    #WHITE BORDER
    Login_button_Border=Label(root, bg="#771EAB")
    Login_button_Border.place(x=100, y=Login_button_y, width=300, height=60)
    
    button_login = Button(root, command=Login_success, text="Login", font=("Comfortaa", 25), fg="white", bg="#440c2c", bd="0",  relief="solid", activebackground="#811B2F", activeforeground="white",)
    button_login.place (x=105, y=Login_button_y + 5 , width=290,height=50)


    
def Login_input(root,Login_input_y):
    Login_button_Border=Label(root, bg="#e4275e")
    Login_button_Border.place(x=100, y=Login_input_y, width=300, height=60)
    
    entry = Entry(root, font=("Comfortaa", 16), fg="#e4275e", bg="#61143a", bd=0, relief="solid", insertbackground="white")
    entry.place(x=105, y=Login_input_y+5, width=290, height=50)

    
def close_on_s(root,event):
    if event.char == 's':
        root.destroy()