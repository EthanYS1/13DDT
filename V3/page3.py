from tkinter import *
from PIL import Image, ImageTk
import sqlite3
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
    
    print(f"Current user: {func.current_user}")
    print(f"Current item: {func.current_item}")

    # Write review button
    func2.write_review(root)

    # --- Reviews Display Section ---
    reviews_frame = Frame(root, bg="#fff")
    reviews_frame.place(x=30, y=200, width=440, height=350)

    # Fetch reviews from database
    conn = sqlite3.connect("reviews.db")
    c = conn.cursor()
    c.execute("SELECT username, review FROM reviews ORDER BY id DESC")
    reviews = c.fetchall()
    conn.close()

    if not reviews:
        Label(reviews_frame, text="No reviews yet.", bg="#fff", fg="#61143a", font=("Comfortaa", 12, "italic")).pack(pady=10)
    else:
        for username, review in reviews:
            Label(
                reviews_frame,
                text=f"{username} | {review}",
                anchor="w",
                justify="left",
                bg="#fff",
                fg="#440c2c",
                font=("Comfortaa", 12)
            ).pack(fill="x", padx=10, pady=5)


    root.mainloop()