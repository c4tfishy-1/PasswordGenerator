#Written in CustomTkinter (rather than Tkinter).
#Allows users to select which characters to be included in the generated password.
#Allows users to switch from light/dark mode.
#Allows users to specify password length. 
#Displays the strength of the generated password to users, based on their selections for length and character sets.

import tkinter as tk
from tkinter import *
import random
import pyperclip 
import customtkinter as ctk

ctk.set_appearance_mode("light") 
ctk.set_default_color_theme("blue") 

root = ctk.CTk()
root.title("Password Generator")

newline = ctk.CTkLabel(root, text=" ")
newline.pack()

switch_state = 0

def switch_mode():
    global switch_state
    switch_state = 1 - switch_state
    if (switch_state == 0):
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")

choose_appearance_mode_button = ctk.CTkButton(root, text="Switch appearance mode (light/dark)", text_color="black", fg_color="red", hover_color="red3", command=switch_mode)
choose_appearance_mode_button.pack()

window_width = 400
window_height = 500

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

def get_length():
    length = length_entry.get()
    return length

# Define checkbutton variables
check_var_uppercase = tk.IntVar()
check_var_numbers = tk.IntVar()
check_var_special = tk.IntVar()

newline = ctk.CTkLabel(root, text="\n")
newline.pack()

#Create label & entry widget for user-specified password length
length_label = ctk.CTkLabel(root, text="Length of password to be generated: ")
length_label.pack()
length_entry = ctk.CTkEntry(root, border_width=2, placeholder_text="    ")
length_entry.pack()

# Create checkbuttons
C1 = ctk.CTkCheckBox(root, text="Include uppercase characters?", border_color="red3", fg_color="red3", hover_color="red2", variable=check_var_uppercase)
C1.pack()

C2 = ctk.CTkCheckBox(root, text="Include numbers?", border_color="red3", fg_color="red3", hover_color="red2", variable=check_var_numbers)
C2.pack()

C3 = ctk.CTkCheckBox(root, text="Include special characters?", border_color="red3", fg_color="red3", hover_color="red2", variable=check_var_special)
C3.pack()

newline = ctk.CTkLabel(root, text="   ")
newline.pack()

password_label = ctk.CTkLabel(root, text="Your new passsword is: ")

password_entry = ctk.CTkEntry(root, border_width=2, placeholder_text="Password")

copied_password = ctk.CTkLabel(root, text="")

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
        generated_password = ''.join(random.choice(password_chars) for _ in range(int(get_length())))  # Generate a password of length 12
        # Update the entry widget with the generated password
        password_entry.delete(0, tk.END)
        password_entry.insert(0, generated_password)
        password_label.pack()
        password_entry.pack()
        strength_label = ctk.CTkLabel(root, text="Password strength: " + strength_indicator(generated_password))
        strength_label.pack()
    else:
        password_entry.configure(text="No characters selected.")

def strength_indicator(password):
    length_score = len(password) >= 12
    lower_score = any(chars.islower() for chars in password)
    upper_score = any(chars.isupper() for chars in password)
    digit_score = any(chars.isdigit() for chars in password)
    special_score = any(not chars.isalnum() for chars in password)
    strength = sum([length_score, lower_score, upper_score, digit_score, special_score])
    if strength <= 1:
        return "Very Weak"
    elif strength == 2:
        return "Weak"
    elif strength == 3:
        return "Moderate"
    elif strength == 4:
        return "Strong"
    else:
        return "Very Strong"

generate_button = ctk.CTkButton(root, text="Generate Password", text_color="black", fg_color="red", hover_color="red3", command=print_selection)
generate_button.pack()

newline = ctk.CTkLabel(root, text="\n")
newline.pack()

def copy_to_clipboard():
    pyperclip.copy(generated_password)  # Copy the generated password
    copied_password.configure(text="Password copied to clipbord!") # Feedback for the user
    copied_password.pack()

# Add a Copy button
copy_button = ctk.CTkButton(root, text="Copy to Clipboard", text_color="black", fg_color="red", hover_color="red3", command=copy_to_clipboard)
copy_button.pack()

newline = ctk.CTkLabel(root, text="\n")
newline.pack()

root.mainloop()