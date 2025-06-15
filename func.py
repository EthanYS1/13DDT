from tkinter import *
from PIL import Image, ImageTk
import page1 as page1


def Login_success(root):
    root.destroy()
    page1.open_page1()
    
    
   
  

def Logo(root,Logo_y):
    BG_image= Image.open("Images\Login_background.png")
    Logo=ImageTk.PhotoImage(BG_image) 
    Logo_label=Label(root, image=Logo)
    Logo_label.place (x=125,y=Logo_y,width=250,height=250)

def Login_button(root, Login_button_y, user_entry, pass_entry):
    Login_button_Border = Label(root, bg="#771EAB")
    Login_button_Border.place(x=100, y=Login_button_y, width=300, height=60)

    def attempt_login():
        username = user_entry.get()
        password = pass_entry.get()
        if check_login(username, password):
            Login_success(root)
        else:
            print("Wrong login!")

    button_login = Button(root,command=attempt_login, text="Login",font=("Comfortaa", 25),fg="white",bg="#440c2c",bd="0",relief="solid",activebackground="#811B2F",activeforeground="white",)
    button_login.place(x=105, y=Login_button_y + 5, width=290, height=50)

    
    
def user_input(root,Login_input_y):
    Login_button_Border=Label(root, bg="#e4275e")
    Login_button_Border.place(x=100, y=Login_input_y, width=300, height=60)
    
    user = Entry(root, font=("Comfortaa", 16), fg="#e4275e", bg="#61143a", bd=0, relief="solid", insertbackground="white")
    user.place(x=105, y=Login_input_y+5, width=290, height=50)
    return user 

def password_input(root,Login_input_y):
    Login_button_Border=Label(root, bg="#e4275e")
    Login_button_Border.place(x=100, y=Login_input_y, width=300, height=60)
    
    password = Entry(root, font=("Comfortaa", 16), fg="#e4275e", bg="#61143a", bd=0, relief="solid", insertbackground="white")
    password.place(x=105, y=Login_input_y+5, width=290, height=50)
    return password 

def check_login(username, password):
    if username == "1" and password == "2":
        return True
    else:
        print("")

    


#------------------------------------------------------------------------------
#Page1

def listing (root, listing_y,image_path,food_text):
    
    
    list_label = Label(root, bg="#800F2F")
    list_label.place(x=15, y=listing_y, width=470, height=250)
    
    
    list_button = Button(list_label, text="Button")
    list_button.place(x=350, y=200, width=100, height=30)
    
    list_image_open = Image.open((image_path))
    resized_image = list_image_open.resize((330,330))
    list_image = ImageTk.PhotoImage(resized_image)
    
    list_image_label = Label(list_label, image=list_image, bg="#800F2F")    
    list_image_label.image = list_image
    list_image_label.place(x=-60, y=-5)
    
    list_text = Label(list_label,wraplength=175, justify="left", text=(food_text), fg="#EAEAEA", bg="#800F2F", font=("Comfortaa", 12, "bold") )
    list_text.place(x=285, y=20)
   
    
    
    
def close_on_s(root,event):
    if event.char == 's':
        root.destroy()