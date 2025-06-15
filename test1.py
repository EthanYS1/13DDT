from tkinter import *

def listing(root, list_text, listing_y):
    listing_frame = Frame(root, bg="#800F2F")
    listing_frame.place(x=15, y=listing_y, width=470, height=250)

    text_label = Label(listing_frame, text=list_text, fg="white", bg="#800F2F", font=("Arial", 16))
    text_label.place(x=20, y=30)

    btn = Button(listing_frame, text="Button", command=lambda: print("Button clicked!"))
    btn.place(x=350, y=30)

    return listing_frame

root = Tk()
root.geometry("500x400")
root.title("Tkinter Listing Example")

listing(root, "Sample List Text", 20)

root.mainloop()
