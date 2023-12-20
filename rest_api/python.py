import tkinter as tk
from tkinter import messagebox

def send_wishes():
    messagebox.showinfo("Birthday Wishes", "Wishing you a fantastic birthday!")

# Create the main window
root = tk.Tk()
root.title("Happy Birthday VDV !")

# Create a label with the birthday message
message_label = tk.Label(root, text="Happy Birthday VDV !", font=("Arial", 16))
message_label.pack(pady=20)

# Create a button for sending wishes
wishes_button = tk.Button(root, text="Send Best Wishes", command=send_wishes)
wishes_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

import tkinter as tk
from tkinter import messagebox

def send_wishes():
    messagebox.showinfo("Birthday Wishes", "Wishing you a fantastic birthday!")

# Create the main window
root = tk.Tk()
root.title("Happy Birthday VDV !")

# Create a label with the birthday message
message_label = tk.Label(root, text="Happy Birthday VDV !", font=("Arial", 16))
message_label.pack(pady=20)

# Create a button for sending wishes
wishes_button = tk.Button(root, text="Send Best Wishes", command=send_wishes)
wishes_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
