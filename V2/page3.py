from tkinter import *
from PIL import Image, ImageTk
import func as func
import func2 as func2
from tkinter import messagebox

def open_page3():
    root = Tk()
    root.title("Foodie")
    root.geometry("500x800")
    root.minsize(500, 800)
    root.maxsize(500, 800)
    
    
    BG = Label(root, bg="#61143a")
    BG.place(x=0, y=0, width=500, height=800)
    
    #debuggy
    print(func.current_user) 
    
    #Write review button
    func2.write_review(root)
    
    # Frame for reviews display
    reviews_frame = Frame(root, bg="#61143a")
    reviews_frame.place(x=50, y=100, width=400, height=650)  # Adjust position and size as needed
    #Text on review frame 
    reviews_text = Text(reviews_frame)
    reviews_text.place(width=400, height=600, x=0, y=0)
    
    
    # Read and display reviews from reviews.txt
    try:
        with open("reviews.txt", "r") as file:
            reviews_content = file.read()
            if reviews_content.strip():  # Check if file is not empty
                reviews_text.insert(END, reviews_content)
            else:
                reviews_text.insert(END, "No reviews yet.")
    except FileNotFoundError:
        reviews_text.insert(END, "No reviews yet. Be the first to write one!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load reviews: {e}")
    
    # Make Text widget read-only
    reviews_text.config(state=DISABLED)
    
    def close_on_s(event):
        if event.char == 's':
            root.destroy()

    root.bind('<Key>', close_on_s)
    root.mainloop()