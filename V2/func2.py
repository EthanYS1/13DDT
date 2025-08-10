from tkinter import *
from PIL import Image, ImageTk
import page1 as page1
import page2 as page2
import page1p5 as page1p5
import page3 as page3
import page4 as page4
from tkinter import messagebox


def restaurant_list(root, listing_y,image_path):
    
    def restaurant_selected():
        
        print(f"Image Path: {image_path}")
        root.destroy()
        page1.open_page1() 
        print("Item Selected")
        
        
    
    
    restaurant_label = Label(root, bg="#800F2F")
    restaurant_label.place(x=15, y=listing_y, width=470, height=250)
    
    restaurant_button = Button(restaurant_label, text="Button", command=restaurant_selected)
    restaurant_button.place(x=350, y=200, width=100, height=30)
    
    restaurant_image_open = Image.open((image_path))
    resized_image = restaurant_image_open.resize((330,330))
    restaurant_image = ImageTk.PhotoImage(resized_image)
     
    restaurant_image_label = Label(restaurant_label, image=restaurant_image, bg="#800F2F")    
    restaurant_image_label.image = restaurant_image
    restaurant_image_label.place(x=-60, y=-5)
    
    restaurant_text = Label(restaurant_label,wraplength=175, justify="left", text=(restaurant_text), fg="#EAEAEA", bg="#800F2F", font=("Comfortaa", 12, "bold") )
    restaurant_text.place(x=285, y=20)

def review_button_label(root):
    review_button_label = Label(root, bg="#800F2F")
    review_button_label.place ( x = 200, 
                               y= 650,
                               width=115,
                               height=60,
                               )
    def openpage3():
        root.destroy()
        page3.open_page3()
    
    review_button= Button(review_button_label, 
                          command=openpage3 ,
                          text= "Reviews",
                          font=("Comfortaa", 15),
                          fg = "white",
                          bg="#800F2F")
    review_button.place(x=10, y=10)
                            
                            
def write_review(root):             
    
    def openpage4():
        root.destroy()
        page4.open_page4()           
    write_review_button= Button(root, 
                            command=openpage4,
                            text= "write_review",
                            font=("Comfortaa", 15),
                            fg = "white",
                            bg="#800F2F")
    write_review_button.place(x=150, y=25, width=200, height=50)                         
            
                        

                            
    