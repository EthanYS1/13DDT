from tkinter import *
from PIL import Image, ImageTk
import page1 as page1
import page2 as page2
import page1p5 as page1p5
from tkinter import messagebox
import sqlite3

#Sqlite setup
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')
conn.commit()

#My database variables 
user_input_entry = None
password_input_entry = None

#Gets user entry and strips of spaces
def signup():
    username = user_input_entry.get().strip()
    password = password_input_entry.get().strip()
    #If there is no input on these, display msg
    if not username or not password:
        messagebox.showwarning("Empty", "Username and password cannot be empty.")
        return
    #Inserting the inputs into the database
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("Success", f"User '{username}' signed up successfully!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", f"Username '{username}' already exists.")
        
#Login        
def login(root, user_input_entry, password_input_entry):
    username = user_input_entry.get().strip()
    password = password_input_entry.get().strip()

    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    result = cursor.fetchone()
    #Sees if user input matches with a result in the database
    if result:
        messagebox.showinfo("Success", f"Welcome back, {username}!")
        root.destroy()
        page1p5.open_page1p5()
    else:
        messagebox.showerror("Failed", "Invalid username or password.")
        
def signup_button(root):
    signup_button_Border = Label(root, bg="#771EAB")
    signup_btn = Button(root, command=signup, text="Sign Up", bg="#440c2c", fg="#EAEAEA", font=("Comfortaa", 12, "bold"), relief=SOLID)
    signup_btn.place(x=210, y=700, width=80, height=40 )
    signup_button_Border.place(x=205, y=695, width=90, height=50)

    
    
def Logo(root,Logo_y):
    BG_image= Image.open("Images\Login_background.png")
    Logo=ImageTk.PhotoImage(BG_image) 
    Logo_label=Label(root, image=Logo)
    Logo_label.place (x=125,y=Logo_y,width=250,height=250)

def Login_button(root, Login_button_y, user_input_entry, pass_input_entry):
    Login_button_Border = Label(root, bg="#771EAB")
    Login_button_Border.place(x=100, y=Login_button_y, width=300, height=60)

    def attempt_login():
       login(root,user_input_entry, pass_input_entry)

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
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    result = cursor.fetchone()
    return result is not None

    


#------------------------------------------------------------------------------
#Page1

def listing (root, listing_y,image_path,food_text, ingred, main_txt, cost):
    
    def item_selected():
        
        item_image = image_path
        item_text = food_text
        main_text = main_txt
        ingredients = ingred
        price = cost
        print(f"Image Path: {image_path}")
        print(f"Food Text: {food_text}")
        print(f"Image Path: {ingred}")
        print(f"Food Text: {main_txt}")
        print(f"Image Path: {cost}")
        root.destroy()
        page2.open_page2(item_image, item_text, ingredients, main_text, price) 
        print("Item Selected")
        
        
    
    
    list_label = Label(root, bg="#800F2F")
    list_label.place(x=15, y=listing_y, width=470, height=250)
    
    list_button = Button(list_label, text="Button", command=item_selected)
    list_button.place(x=350, y=200, width=100, height=30)
    
    list_image_open = Image.open((image_path))
    resized_image = list_image_open.resize((330,330))
    list_image = ImageTk.PhotoImage(resized_image)
     
    list_image_label = Label(list_label, image=list_image, bg="#800F2F")    
    list_image_label.image = list_image
    list_image_label.place(x=-60, y=-5)
    
    list_text = Label(list_label,wraplength=175, justify="left", text=(food_text), fg="#EAEAEA", bg="#800F2F", font=("Comfortaa", 12, "bold") )
    list_text.place(x=285, y=20)
    
#-------------------------------------------------------------
 #page 2
 

        
def close_on_s(root,event):
    if event.char == 's':
        root.destroy()