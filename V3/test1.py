import sqlite3
import tkinter as tk
from tkinter import simpledialog, messagebox
import func   # <-- using your current_user variable

# --- Database setup ---
conn = sqlite3.connect("reviews.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS reviews (item TEXT, username TEXT, review TEXT)")
conn.commit()

# --- Tkinter setup ---
root = tk.Tk()
root.title("Review App")
root.geometry("400x400")

# --- Page handling ---
frames = {}
current_item = None

# --- Functions ---
def show_frame(name):
    frame = frames[name]
    frame.tkraise()

def open_reviews(item):
    global current_item
    current_item = item
    refresh_reviews()
    show_frame("page2")

def refresh_reviews():
    for widget in frames["page2"].winfo_children():
        widget.destroy()
    
    tk.Label(frames["page2"], text=f"Reviews for {current_item}", font=("Arial", 16)).pack(pady=10)
    
    # fetch reviews
    c.execute("SELECT username, review FROM reviews WHERE item=?", (current_item,))
    rows = c.fetchall()
    if rows:
        for r in rows:
            tk.Label(frames["page2"], text=f"{r[0]}: {r[1]}", wraplength=350, justify="left").pack(anchor="w", padx=10)
    else:
        tk.Label(frames["page2"], text="No reviews yet.").pack()
    
    tk.Button(frames["page2"], text="Write Review", command=lambda: show_frame("page3")).pack(pady=10)
    tk.Button(frames["page2"], text="Back", command=lambda: show_frame("page1")).pack()

def save_review(text):
    if text.strip() == "":
        messagebox.showwarning("Empty", "Review cannot be empty.")
        return
    c.execute("INSERT INTO reviews (item, username, review) VALUES (?, ?, ?)", (current_item, func.current_user, text))
    conn.commit()
    show_frame("page2")
    refresh_reviews()

# --- Page 1 ---
page1 = tk.Frame(root)
frames["page1"] = page1
page1.place(relx=0, rely=0, relwidth=1, relheight=1)

btn1 = tk.Button(page1, text="Item A", command=lambda: open_reviews("Item A"))
btn1.pack(pady=20)
btn2 = tk.Button(page1, text="Item B", command=lambda: open_reviews("Item B"))
btn2.pack(pady=20)

# --- Page 2 (reviews) ---
page2 = tk.Frame(root)
frames["page2"] = page2
page2.place(relx=0, rely=0, relwidth=1, relheight=1)

# --- Page 3 (write review) ---
page3 = tk.Frame(root)
frames["page3"] = page3
page3.place(relx=0, rely=0, relwidth=1, relheight=1)

tk.Label(page3, text="Write your review:", font=("Arial", 14)).pack(pady=10)
review_entry = tk.Text(page3, height=8, width=40)
review_entry.pack()

tk.Button(page3, text="Save", command=lambda: (save_review(review_entry.get("1.0", tk.END)), review_entry.delete("1.0", tk.END))).pack(pady=5)
tk.Button(page3, text="Cancel", command=lambda: show_frame("page2")).pack()

# --- Start ---
show_frame("page1")
root.mainloop()
