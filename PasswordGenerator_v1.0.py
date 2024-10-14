import tkinter as tk
from tkinter import *
import random
import pyperclip 


root = tk.Tk()
root.title("Password Generator")

window_width = 300
window_height = 200

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

def get_lowercase_chars():
    return "abcdefghijklmnopqrstuvwxyz"

def get_uppercase_chars():
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_nums():
    return "1234567890"

def get_special_chars():
    return "!@#$%^&*"

# Define checkbutton variables
check_var_uppercase = tk.IntVar()
check_var_numbers = tk.IntVar()
check_var_special = tk.IntVar()

# Create checkbuttons
C1 = tk.Checkbutton(root, text="Include uppercase characters?", variable=check_var_uppercase)
C1.pack()

C2 = tk.Checkbutton(root, text="Include numbers?", variable=check_var_numbers)
C2.pack()

C3 = tk.Checkbutton(root, text="Include special characters?", variable=check_var_special)
C3.pack()

# Label to display the generated password
password_label = tk.Label(root, text="")
password_label.pack()

# Function to generate password based on selections
def print_selection():
    global generated_password  # Declare as global to use in copy function
    password_chars = get_lowercase_chars()  # Start with lowercase

    if check_var_uppercase.get():
        password_chars += get_uppercase_chars()
    if check_var_numbers.get():
        password_chars += get_nums()
    if check_var_special.get():
        password_chars += get_special_chars()

    if password_chars:  # Check if any characters are selected
        generated_password = ''.join(random.choice(password_chars) for _ in range(12))  # Generate a password of length 12
        password_label.config(text="New password: " + generated_password)  # Update the label with the generated password
    else:
        password_label.config(text="No characters selected to generate a password.")
    
# Function to copy the generated password to clipboard
def copy_to_clipboard():
    pyperclip.copy(generated_password)  # Copy the generated password
    #print("Password copied to clipboard!")  # Feedback for the user
    copied_password = tk.Label(root, text="Password copied to clipboard!")
    copied_password.place(x=70, y=150)

generate_button = tk.Button(root, text="Generate Password", command=print_selection)
generate_button.pack()

# Add a Copy button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack()


root.mainloop()