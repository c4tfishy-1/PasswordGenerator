A simple password generator, written in Python. This script requires various modules, which can be installed using the instructions below:
1. Open a command prompt or terminal.
2. Type `pip install customtkinter`, and press Enter.
3. Type `pip install pyperclip`, and press Enter.
4. As both the random module and Tkinter are built-in modules, they do not need to be installed via Pip.

Usage:
1. Locate the script in its folder within your files (eg. Downloads).
2. Double-click the file to run the script.
3. A window will appear with several options available for the user to select.
   The user must specify a password length. If none of the checkboxes (for uppercase, numerical and special characters) are selected,
   the generated password will be all lowercase by default. 
4. Click "Generate Password" to generate the new password. The strength indicator label will indicate the strength of the generated password.
    If the generated password's strength is not desirable, a new (and stronger) password can be generated by entering a greater value for password length and selecting
    more checkboxes.
5. Click "Copy to Clipboard" to copy the generated password.
6. Paste the generated password anywhere - for example, into a password manager.
7. Done!

For an example of the PasswordGenerator in action, refer to the image below:

![image](https://github.com/user-attachments/assets/6365de4d-6733-475a-8e32-0c565091669f)

In this image, the password generated (by specifying a length of 12 and including only numbers as well as the default lowercase characters) has a moderate strength. 
This could be increased by selecting the other two checkboxes:

![image](https://github.com/user-attachments/assets/5a19645f-b39a-4449-8e53-cd8e5014471d)

Once the checkboxes for uppercase and special characters are selected, the password strength changes from Moderate to Strong. 

Enjoy!
