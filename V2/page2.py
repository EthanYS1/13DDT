from tkinter import *
from PIL import Image, ImageTk
import func as func
import func2 as func2

def open_page2(item_image, item_text, ingredients, main_text, price):
    root = Tk()
    root.title("Foodie")
    root.geometry("500x800")
    root.minsize("500","800")
    root.maxsize("500","800")
    
    BG= Label(root, bg="#61143a")
    BG.place(x=0,y=0,width=500,height=800)
    
    print({func.current_user})
     
    c_img1 = Image.open(item_image)
    c_img1 = c_img1.resize((350,350))
    c_img2 = ImageTk.PhotoImage(c_img1)
    c_img_label = Label(root,image=c_img2)
    c_img_label.place(x=75,y=35)
    item_description = Label(root)
    item_description.place (x=75, y=400, width=350, height=200)
    
    #Title- big - bold
    Label(item_description, text=item_text, font=("Helvetica", 16, "bold")).place(x=75,y=10)
   
    # main text
    Label(item_description, text=main_text, font=("Helvetica", 12)).place(x=35,y=50)     
        
    #ingredients - 
    Label(item_description, text=ingredients, font=("Helvetica", 12, "bold")).place(x=25,y=85)


    # price - bold
    Label(item_description, text=price, font=("Helvetica", 12, "bold")).place(x=150,y=125)
        
    func2.review_button_label(root)
    
    
    def close_on_s(event):
        if event.char == 's':
            root.destroy()

    root.bind('<Key>', close_on_s)
    root.mainloop()

    



