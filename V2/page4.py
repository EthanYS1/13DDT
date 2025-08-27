from tkinter import *
from PIL import Image, ImageTk
import func as func
import func2 as func2
import page2 as page2

def open_page4():
    root = Tk()
    root.title("Foodie")
    root.geometry("500x800")
    root.minsize("500","800")
    root.maxsize("500","800")
    
    BG= Label(root, bg="#61143a")
    BG.place(x=0,y=0,width=500,height=800)
     
    def review_list():
        review_list_background=Label(root, bg="#FFFFFF")
        review_list_background.place(x=0,y=100,width=500,height=800)
        
    review_list()     
         
    #WRITE REVIEW ENTRY BOX
    Label(root, text="Write your review:", bg="#00FFAE").place(x=10, y=160)
    review_entry = Text(root, width=40, height=10)
    review_entry.place(x=10, y=190)
    
    #Submit review button
    
    def submit_review():
        review = review_entry.get("1.0", END).strip()

        
        with open("reviews.txt", "a", encoding="utf-8") as f:
            f.write(f"{func.current_user}||{review}\n")
        root.destroy()

    Button(root, text="Submit Review", command=submit_review).place(x=180, y=400)
    
    
    def close_on_s(event):
        if event.char == 's':
            root.destroy()

    root.bind('<Key>', close_on_s)
    root.mainloop()

    



