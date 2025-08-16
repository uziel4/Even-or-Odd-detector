"""
Author: Uziel E. Santos
Description: This code provides the combination of frontend and backend. In this code you will find the elaboration of a simple calculator utilizing tkinter as out GUI.
Date: 2025/08/16
"""

import math
import tkinter

# Here the buttons are defined in matrix form
button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

# Here we establish the symbols that are on the right of our GUI
symbols_on_the_right =  ["÷", "×", "-", "+", "=","√"]

# Here we establish the symbols that are on the top of our GUI
symbols_on_top = ["AC","+/-","%"]

# Colors for our calculator
light_gray = "#D4D4D2"
black = "#1C1C1C"
dark_gray = "#505050"
orange = "#FF9500"
white = "white"

#Row and columns counts based on the button_values
row_count = len(button_values)
column_count = len(button_values[0])

# ______ Window Setup ----- #
# Creation of our main window
window = tkinter.Tk()
# Assigning a title to our window
window.title("Calculator")
# Here we don't let the user resize the window
window.resizable(False,False)

# Creating the background frame
frame = tkinter.Frame(window)

# This is the display label of the calculator that acts as the screen
label = tkinter.Label(frame, text = "0", font= ("Arial",45), background=black,
                      foreground= white,anchor="e",width=column_count)
label.grid(row = 0,column=0,columnspan=column_count,sticky="we")

# ----- Button creation ----- #
for row in range(row_count):
    # This loop generates all buttons dynamically from button_values
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame,text = value, font = ("Arial",30),
                                width=column_count-1, height= 1,
                                command=lambda value = value: button_clicked(value))
        # Color assignment depending on the position of the buttons
        if value in symbols_on_top:
            button.config(foreground=black,background=light_gray)
        elif value in symbols_on_the_right:
            button.config(foreground=white,background=orange)
        else:
            button.config(foreground=white,background=dark_gray)
        # Place the button on the grid
        button.grid(row=row+1,column=column)

frame.pack()

# ----- Global Variables ----- #
A = 0 # Stores the first digit
operator = None # Stores the selected operand
B = None # Stores the second digit

# ----- Helper Functions ------ #
# This function reset all the stored values
def clear_all():
    global A , B, operator
    A = 0
    operator = None
    B = None
# This function remove the decimal ".0" if the number is an integer
def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)

# ----- Main Logic ----- #
# This function is executed everytime a buttons is clicked
def button_clicked(value):
    global symbols_on_the_right , symbols_on_top, label, A, B, operator

    if value in symbols_on_the_right:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    label["text"] = remove_zero_decimal(numA+numB)
                elif operator == "-":
                    label["text"] = remove_zero_decimal(numA-numB)
                elif operator == "×":
                    label["text"] = remove_zero_decimal(numA * numB)
                elif operator == "÷":
                    label["text"] = remove_zero_decimal(numA / numB)


                clear_all()
        elif value == "√":
            try:
                num = float(label["text"])
                if num <0:
                    label["text"] = "Error"
                    clear_all()
                else:
                    label["text"] = remove_zero_decimal(math.sqrt(num))
            except ValueError:
                label["text"] = "O"
            return

        elif value in "+-×÷√":
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"

            operator = value

    # ----- Handle top row functions ----- #
    elif value in symbols_on_top:
        if value == "AC":
            clear_all()
            label["text"] = "0"

        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)
        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)
    else: #digits or .
        if value == ".":
            if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value #This replaces the 0
            else:
                label["text"] += value #appends the digit






# ----- Centering the window ----- #
window.update() # This update the width of the window with the new size dimensions
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2)-window_width/2)
window_y = int((screen_height/2)-window_height/2)

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# This keep the window open
window.mainloop()



if __name__ == "_main_":
    pass
