import sqlite3
from tkinter import *
from tkinter import messagebox

# === SETUP DATABASE ===
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

# === FUNCTIONS ===
def sign_up():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not username or not password:
        messagebox.showwarning("Empty", "Username and password cannot be empty.")
        return

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("Success", f"User '{username}' signed up successfully!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", f"Username '{username}' already exists.")

def log_in():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Success", f"Welcome back, {username}!")
    else:
        messagebox.showerror("Failed", "Invalid username or password.")

# === GUI SETUP ===
root = Tk()
root.title("Login/Signup System")
root.geometry("300x250")

# Username label + entry
username_label = Label(root, text="Username:")
username_label.pack(pady=(15, 0))
username_entry = Entry(root)
username_entry.pack(pady=5)

# Password label + entry
password_label = Label(root, text="Password:")
password_label.pack(pady=(10, 0))
password_entry = Entry(root, show="*")  # show="*" hides the password
password_entry.pack(pady=5)

# Buttons
signup_btn = Button(root, text="Sign Up", command=sign_up)
signup_btn.pack(pady=10)

login_btn = Button(root, text="Log In", command=log_in)
login_btn.pack()

root.mainloop()
