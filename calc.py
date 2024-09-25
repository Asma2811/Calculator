import tkinter as tk
from tkinter import messagebox

# Calculator class
class Calculator:
    def __init__(self, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2

    def set_numbers(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2

    def divide(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            return "Error"

    def multiply(self):
        return self.num1 * self.num2

# Function to handle button clicks
def on_button_click(value):
    current = entry_display.get()
    
    if value == "C":
        entry_display.delete(0, tk.END)
    elif value == "=":
        try:
            if "+" in current:
                num1, num2 = map(float, current.split("+"))
                calc.set_numbers(num1, num2)
                result = calc.add()
            elif "-" in current:
                num1, num2 = map(float, current.split("-"))
                calc.set_numbers(num1, num2)
                result = calc.subtract()
            elif "/" in current:
                num1, num2 = map(float, current.split("/"))
                calc.set_numbers(num1, num2)
                result = calc.divide()
            elif "*" in current:
                num1, num2 = map(float, current.split("*"))
                calc.set_numbers(num1, num2)
                result = calc.multiply()
            else:
                result = "Error"
            
            entry_display.delete(0, tk.END)
            entry_display.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")   
    else:
        entry_display.insert(tk.END, value)

# Creating the main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg="#2b2b2b")

# Creating an instance of the Calculator class
calc = Calculator()

# Display Entry (to show the expression and result)
entry_display = tk.Entry(root, width=20, font=('Courier', 24), borderwidth=5, relief='flat', justify='right')
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=8, ipady=8)

# Button properties
button_colors = {
    "number_bg": "#4e4e4e",  # Dark gray for number buttons
    "operator_bg": "#f39c12",  # Bright orange for operators
    "special_bg": "#e74c3c",   # Red for clear
    "equal_bg": "#2ecc71",     # Green for equals
    "text_color": "#ffffff"    # White text color for all buttons
}

# Buttons for the calculator
buttons = [
    ("7", button_colors["number_bg"], button_colors["text_color"]), 
    ("8", button_colors["number_bg"], button_colors["text_color"]), 
    ("9", button_colors["number_bg"], button_colors["text_color"]), 
    ("/", button_colors["operator_bg"], button_colors["text_color"]),
    
    ("4", button_colors["number_bg"], button_colors["text_color"]), 
    ("5", button_colors["number_bg"], button_colors["text_color"]), 
    ("6", button_colors["number_bg"], button_colors["text_color"]), 
    ("*", button_colors["operator_bg"], button_colors["text_color"]),
    
    ("1", button_colors["number_bg"], button_colors["text_color"]), 
    ("2", button_colors["number_bg"], button_colors["text_color"]), 
    ("3", button_colors["number_bg"], button_colors["text_color"]), 
    ("-", button_colors["operator_bg"], button_colors["text_color"]),
    
    ("C", button_colors["special_bg"], button_colors["text_color"]), 
    ("0", button_colors["number_bg"], button_colors["text_color"]), 
    ("=", button_colors["equal_bg"], button_colors["text_color"]), 
    ("+", button_colors["operator_bg"], button_colors["text_color"])
]

# Add buttons to the window in a grid with colors
row_value = 1
col_value = 0

for (text, bg_color, fg_color) in buttons:
    tk.Button(root, text=text, width=5, height=2, font=('Courier', 18), 
              bg=bg_color, fg=fg_color, relief="flat", 
              activebackground=bg_color, activeforeground=fg_color,
              command=lambda x=text: on_button_click(x)).grid(row=row_value, column=col_value, 
                                                              padx=5, pady=5, ipadx=10, ipady=10)
    col_value += 1
    if col_value > 3:
        col_value = 0
        row_value += 1

# Running the application
root.mainloop()

