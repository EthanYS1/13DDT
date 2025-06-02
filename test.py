# main.py
from tkinter import *
from PIL import Image, ImageTk
import openpls  # Importing the second page

root = Tk()
root.title("Foodie")
root.geometry("500x800")
root.minsize("500", "800")
root.maxsize("500", "800")

# Background image
BG_image = Image.open("Ethan_13DDT_/Images/LGBG.png")
Resized_BG_image = BG_image.resize((1000, 1000))
BG = ImageTk.PhotoImage(Resized_BG_image)

BGLabel = Label(root, image=BG)
BGLabel.place(x=-300, y=0)

# On login success
def Login_success():
    root.destroy()        # Close current window
    openpls.openpls()     # Open the second page

# Logo function
def Logo(Logo_y):
    Logo_img = Image.open("Ethan_13DDT_/Images/LGBG.png")
    Logo_img = Logo_img.resize((250, 250))
    Logo = ImageTk.PhotoImage(Logo_img)
    Logo_label = Label(root, image=Logo)
    Logo_label.image = Logo  # Prevent garbage collection
    Logo_label.place(x=125, y=Logo_y, width=250, height=250)

# Login button
def Login_button(y):
    Label(root, bg="#771EAB").place(x=100, y=y, width=300, height=60)
    Button(
        root,
        text="Login",
        command=Login_success,
        font=("Comfortaa", 25),
        fg="white",
        bg="#440c2c",
        bd=0,
        relief="solid",
        activebackground="#811B2F",
        activeforeground="white"
    ).place(x=105, y=y + 5, width=290, height=50)

# Input field
def Login_input(y):
    Label(root, bg="#e4275e").place(x=100, y=y, width=300, height=60)
    Entry(
        root,
        font=("Comfortaa", 16),
        fg="#e4275e",
        bg="#61143a",
        bd=0,
        relief="solid",
        insertbackground="white"
    ).place(x=105, y=y + 5, width=290, height=50)

# Draw widgets
Login_input(370)  # Username
Login_input(470)  # Password
Login_button(600)
Logo(50)

# Press 's' to close window
def close_on_s(event):
    if event.char == 's':
        root.destroy()

root.bind('<Key>', close_on_s)
root.mainloop()
