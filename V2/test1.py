import tkinter as tk
from tkinter import scrolledtext
import os

# File to store saved entries
SAVE_FILE = "saved_text.txt"

def load_saved_entries():
    """Load all saved entries from file as a list."""
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r", encoding="utf-8") as file:
            return file.read().splitlines()
    return []

def save_entries(entries):
    """Save all entries back to the file."""
    with open(SAVE_FILE, "w", encoding="utf-8") as file:
        file.write("\n".join(entries))

def on_submit():
    """Handle new entry submission."""
    new_text = entry.get().strip()
    if new_text:
        all_entries.append(new_text)
        save_entries(all_entries)
        update_display()
        entry.delete(0, tk.END)

def update_display():
    """Update the text display area with all entries."""
    text_display.config(state='normal')  # Enable editing
    text_display.delete(1.0, tk.END)     # Clear current text
    for line in all_entries:
        text_display.insert(tk.END, line + "\n")
    text_display.config(state='disabled')  # Make it read-only

# -------------------------------
# GUI Setup
# -------------------------------
root = tk.Tk()
root.title("Entry Logger")
root.geometry("600x500")  # Long window

# Entry box
entry = tk.Entry(root, width=60)
entry.pack(pady=10)

# Submit button
submit_btn = tk.Button(root, text="Submit", command=on_submit)
submit_btn.pack(pady=5)

# Scrollable text display
text_display = scrolledtext.ScrolledText(root, width=70, height=20, state='disabled', wrap='word')
text_display.pack(pady=10)

# Load entries on start
all_entries = load_saved_entries()
update_display()

# Start the GUI event loop
root.mainloop()
