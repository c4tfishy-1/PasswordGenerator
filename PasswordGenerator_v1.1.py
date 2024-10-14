#Written in CustomTkinter (rather than Tkinter).

import tkinter as tk
from tkinter import *
import random
import pyperclip 
import customtkinter as ctk

ctk.set_appearance_mode("light") 
ctk.set_default_color_theme("blue") 

root = ctk.CTk()
root.title("Password Generator")

window_width = 300
window_height = 400

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

newline = ctk.CTkLabel(root, text="\n")
newline.pack()

# Create checkbuttons
C1 = ctk.CTkCheckBox(root, text="Include uppercase characters?", border_color="black", fg_color="hot pink", hover_color="pink", variable=check_var_uppercase)
C1.pack()

C2 = ctk.CTkCheckBox(root, text="Include numbers?", border_color="black", fg_color="hot pink", hover_color="pink", variable=check_var_numbers)
C2.pack()

C3 = ctk.CTkCheckBox(root, text="Include special characters?", border_color="black", fg_color="hot pink", hover_color="pink", variable=check_var_special)
C3.pack()

newline = ctk.CTkLabel(root, text="\n")
newline.pack()

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
        password_label.configure(text="New password: " + generated_password)  # Update the label with the generated password
    else:
        password_label.configure(text="No characters selected to generate a password.")

generate_button = ctk.CTkButton(root, text="Generate Password", text_color="black", fg_color="pink", hover_color="hot pink", command=print_selection)
generate_button.pack()

newline = ctk.CTkLabel(root, text="\n")
newline.pack()

def copy_to_clipboard():
    pyperclip.copy(generated_password)  # Copy the generated password
    #print("Password copied to clipboard!")  # Feedback for the user
    copied_password.configure(text="Password copied to clipbord!")

# Add a Copy button
copy_button = ctk.CTkButton(root, text="Copy to Clipboard", text_color="black", fg_color="pink", hover_color="hot pink", command=copy_to_clipboard)
copy_button.pack()

newline = ctk.CTkLabel(root, text="\n")
newline.pack()

password_label = ctk.CTkLabel(root, text="")
password_label.pack()

copied_password = ctk.CTkLabel(root, text="")
#copied_password.pack()
copied_password.pack()

root.mainloop()