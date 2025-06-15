from tkinter import *
from PIL import Image, ImageTk


def listing (root, listing_y):
    
    
    list_label = Label(root, bg="#800F2F")
    list_label.place(x=15, y=listing_y, width=470, height=250)
    
    
    list_button = Button(list_label, text="Button")
    list_button.place(x=350, y=200, width=100, height=30)
    
    list_image_open = Image.open("Images\Login_background.png")
    resized_image = list_image_open.resize((400,220))
    list_image = ImageTk.PhotoImage(resized_image)
    
    list_image_label = Label(list_label, image=list_image, bg="#800F2F")    
    list_image_label.image = list_image
    list_image_label.place(x=-65, y=10)
    
    list_text = Label(list_label,wraplength=175, justify="left", text="WOAH WOAH WOAH, BEN?, NO, YES, LALALAHA, BEN?, No, No, NO, NO, HOHOHO, HOHOHOHO", fg="#EAEAEA", bg="#800F2F", font=("Comfortaa", 12, "bold") )
    list_text.place(x=275, y=20)
   
    
root = Tk()
root.geometry("500x800")
root.title("Tkinter Listing Example")


label_listing = Label(root, width= 500, height=800, bg="#61143a")
label_listing.place(x=0, y=0)


listing(root, 20)   

root.mainloop()