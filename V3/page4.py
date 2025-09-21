from tkinter import *
import func as func
import func2 as func2
import page2 as page2
import page3 as page3
from tkinter import messagebox

def open_page4():
    root = Tk()
    root.title("Foodie - Write Review")
    root.geometry("500x800")
    root.minsize("500","800")
    root.maxsize("500","800")
    
    BG= Label(root, bg="#61143a")
    BG.place(x=0,y=0,width=500,height=800)
    
    # Title
    title_label = Label(root, text="Write Review", fg="#EAEAEA", bg="#61143a", 
                       font=("Comfortaa", 20, "bold"))
    title_label.place(x=175, y=30)
    
    # Current user and item info
    user_label = Label(root, text=f"User: {func.current_user}", fg="#e4275e", bg="#61143a", 
                      font=("Comfortaa", 12, "bold"))
    user_label.place(x=20, y=80)

    
    # Review text area
    review_label = Label(root, text="Your Review:", fg="#EAEAEA", bg="#61143a", 
                        font=("Comfortaa", 14, "bold"))
    review_label.place(x=20, y=160)
    
    # Text area frame with border
    text_frame = Frame(root, bg="#e4275e")
    text_frame.place(x=20, y=190, width=460, height=400)
    
    # Text widget
    review_text = Text(text_frame, font=("Comfortaa", 12), fg="#000000", bg="#FFFFFF", 
                      wrap=WORD, relief=FLAT, bd=5)
    review_text.place(x=5, y=5, width=450, height=390)
    
    # Submit button
    def submit_review():
        review_content = review_text.get("1.0", END).strip()
        
        if not review_content:
            messagebox.showwarning("Empty Review", "Can not leave review blank")
            return
        
        if not func.current_user:
            messagebox.showerror("Error", "No user logged in.")
            return
            
        # Save review to database
        if func.save_review(review_content):
            messagebox.showinfo("Success", "Review submitted successfully!")
            root.destroy()
            page3.open_page3()  # Go back to reviews page
        else:
            messagebox.showerror("Error", "Failed to submit review. Please try again.")
    
    submit_btn = Button(root, text="Submit Review", command=submit_review,
                       bg="#800F2F", fg="#EAEAEA", font=("Comfortaa", 16, "bold"))
    submit_btn.place(x=150, y=620, width=200, height=50)
    
    # Back button
    def go_back():
        root.destroy()
        page3.open_page3()

    back_btn = Button(root, text="Back", command=go_back,
                     bg="#440c2c", fg="#EAEAEA", font=("Comfortaa", 12, "bold"))
    back_btn.place(x=20, y=720, width=80, height=40)

    root.mainloop()