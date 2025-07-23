import time
import random
from tkinter import Tk, Label, Button, Entry, messagebox
from plyer import notification

# Function to display a motivational message
def display_motivational_message():
    messages = [
        "A short break now will boost your productivity later!",
        "Taking breaks is essential for maintaining focus and creativity!",
        "Rest and self-care are important for your mental and physical well-being!",
        "Remember to take a break and recharge!",
        "Give yourself permission to take breaks - you deserve it!",
        "Step away from your work for a moment and breathe!",
        "Taking breaks helps prevent burnout and improves overall well-being!",
    ]
    message = random.choice(messages)
    notification.notify(
        title="Take a Break",
        message=message,
        timeout=10
    )

# Function to start the break timer
def start_break_timer():
    try:
        duration = int(entry.get()) * 60  # Convert minutes to seconds
        messagebox.showinfo("Break Timer", f"Break timer set for {entry.get()} minutes")
        root.after(duration * 1000, display_motivational_message)  # Schedule the notification after the duration
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid duration")

# GUI setup
root = Tk()
root.title("Take a Break")

# Styling
root.geometry("300x200")  # Set window size
root.configure(bg="#f0f0f0")  # Set background color

# Title label
title_label = Label(root, text="Take a Break", font=("Helvetica", 20), bg="#f0f0f0")
title_label.pack(pady=10)

# Instruction label
instruction_label = Label(root, text="Enter break duration (minutes):", font=("Helvetica", 12), bg="#f0f0f0")
instruction_label.pack()

# Entry widget
entry = Entry(root, width=10, font=("Helvetica", 12))
entry.pack()

# Button widget
button = Button(root, text="Start Break", command=start_break_timer, font=("Helvetica", 12))
button.pack(pady=10)

root.mainloop()