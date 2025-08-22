"""
Author: Uziel E. Santos 
Description: This script contains functions to encrypt and decrypt text. Using base64 encoding for encryption and decoding, and tkinter for the GUI.
Date: 2025/08/21
"""

from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    """
    Decrypts the text from the main input box using base64 decoding.
    Requires the correct password ("1234") to proceed.
    Shows the decrypted text in a new window.
    Displays error messages for empty or incorrect passwords.
    """
    password = code.get()
    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("DECRYPTION")
        screen2.geometry("400x200")
        screen2.config(bg="#00bd56")

        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypted = base64_bytes.decode("ascii")

        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
        text2 = Text(screen2, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypted)
    elif password == "":
        messagebox.showerror("Error", "Input the secret key")
    else:
        messagebox.showerror("Error", "Incorrect secret key")
    

def encrypt():
    """
    Encrypts the text from the main input box using base64 encoding.
    Requires the correct password ("1234") to proceed.
    Shows the encrypted text in a new window.
    Displays error messages for empty or incorrect passwords.
    """
    password = code.get()
    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("ENCRYPTION")
        screen1.geometry("400x200")
        screen1.config(bg="#ed3833")

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypted = base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPTED", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypted)
    elif password == "":
        messagebox.showerror("Error", "Input the secret key")
    else:
        messagebox.showerror("Error", "Incorrect secret key")


def main_screen():
    """
    Initializes the main GUI window for encryption and decryption.
    Sets up input fields, buttons, and window properties.
    Handles window centering and minimum size.
    """
    global screen, code, text1   

    screen = Tk()

    screen.geometry("375x398")

    #icon 
    image_icon = PhotoImage(file="/Users/uzielsantos/Desktop/VSCODEPYTHON/Juego/Encryption and Decryption.py/keys.jpeg")
    screen.iconphoto(False, image_icon)
    screen.title("Encryption and Decryption")

    def rest():
        """
        Resets the input fields for text and password.
        """
        code.set("")
        text1.delete(1.0, END)


    Label(text="Enter text for encryption and decryption", fg = "black" , font = ("calibri",13)).place(x = 10, y =10)
    text1 = Text(font="Robo 20", bg="white", relief=GROOVE, bd = 0)
    text1.place(x = 10, y = 50, width = 355, height = 100)

    Label(text = "Enter secret key for encryption and decryption", fg = "black", font = ("calibri",13)).place(x = 10, y = 170)

    code = StringVar()
    Entry(textvariable=code, width=25,bd=0, font=("arial", 25),show="*").place(x = 10, y = 200)

    Button(screen, text="Encrypt", height=2, width=23, highlightbackground="#ed3833", fg="white", bd=0,command=encrypt).place(x=10, y=250)
    Button(screen, text="Decrypt", height=2, width=23, highlightbackground="#00bd56", fg="white", bd=0,command=decrypt).place(x=250, y=250)
    Button(text="Reset", height=2, width=50, highlightbackground="#1089ff", fg="white", bd=0, command=rest).place(x=10, y=300)

    # Center the window on the screen
    # Center the window on the screen and set a minimum size
    screen.update_idletasks()
    width = screen.winfo_reqwidth()
    height = screen.winfo_reqheight()
    min_width = 500
    min_height = 500
    screen.minsize(min_width, min_height)
    x = (screen.winfo_screenwidth() // 2) - (width // 2)
    y = (screen.winfo_screenheight() // 2) - (height // 2)
    screen.geometry(f"{width}x{height}+{x}+{y}")


    screen.mainloop()

   
if __name__ == "__main__":
    main_screen()
    