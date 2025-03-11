import tkinter as tk
import math

# Colors and Fonts
BG_COLOR = "#2C3E50"  # Dark Blue Gray (Dark Mode)
BUTTON_COLOR = "#3498DB"  # Blue Buttons
BUTTON_HOVER = "#2980B9"  # Darker Blue
FONT_STYLE = ("Arial", 16)
TEXT_COLOR = "white"

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x600")
        self.root.configure(bg=BG_COLOR)

        self.expression = ""
        self.result_shown = False
        self.memory = 0  # Memory storage

        # Entry Field
        self.entry = tk.Entry(root, font=("Arial", 24), bd=10, relief="ridge", justify="right", width=16, bg="#1C2833", fg="white")
        self.entry.grid(row=0, column=0, columnspan=5, pady=10, padx=10, ipadx=5, ipady=10)

        # Calculator Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('⌫', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('M+', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3), ('M-', 4, 4),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('√', 5, 3), ('MR', 5, 4),
            ('%', 6, 0), ('^', 6, 1), ('(', 6, 2), (')', 6, 3), ('MC', 6, 4)
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

        # Keyboard Support
        root.bind("<Key>", self.keyboard_input)

    def create_button(self, text, row, col):
        """Create buttons with hover effects."""
        btn = tk.Button(self.root, text=text, font=FONT_STYLE, bg=BUTTON_COLOR, fg=TEXT_COLOR,
                        width=5, height=2, relief="raised", command=lambda: self.on_button_click(text))
        btn.grid(row=row, column=col, padx=5, pady=5)
        btn.bind("<Enter>", lambda e: btn.config(bg=BUTTON_HOVER))
        btn.bind("<Leave>", lambda e: btn.config(bg=BUTTON_COLOR))

    def on_button_click(self, value):
        """Handles button clicks."""
        if value == "=":
            try:
                self.expression = self.evaluate_expression(self.expression)
                self.result_shown = True
            except:
                self.expression = "Error"
        elif value == "C":
            self.expression = ""
            self.result_shown = False
        elif value == "⌫":
            self.expression = self.expression[:-1]
        elif value == "M+":
            self.memory += float(eval(self.expression)) if self.expression else 0
        elif value == "M-":
            self.memory -= float(eval(self.expression)) if self.expression else 0
        elif value == "MR":
            self.expression = str(self.memory)
        elif value == "MC":
            self.memory = 0
        else:
            if self.result_shown:
                self.expression = ""
                self.result_shown = False
            self.expression += value

        self.update_entry()

    def evaluate_expression(self, expr):
        """Evaluates math functions and expressions."""
        expr = expr.replace("^", "**")
        expr = expr.replace("√", "math.sqrt")
        expr = expr.replace("sin", "math.sin(math.radians")
        expr = expr.replace("cos", "math.cos(math.radians")
        expr = expr.replace("tan", "math.tan(math.radians")

        if "math.sin(" in expr or "math.cos(" in expr or "math.tan(" in expr:
            expr += ")"

        return str(eval(expr))

    def keyboard_input(self, event):
        """Handles keyboard input."""
        key = event.char
        if key in "0123456789+-*/().^":
            if self.result_shown:
                self.expression = ""
                self.result_shown = False
            self.expression += key
        elif key == "\r":  # Enter key
            try:
                self.expression = self.evaluate_expression(self.expression)
                self.result_shown = True
            except:
                self.expression = "Error"
        elif key == "\x08":  # Backspace
            self.expression = self.expression[:-1]
        elif key.lower() == "c":
            self.expression = ""
            self.result_shown = False
        self.update_entry()

    def update_entry(self):
        """Updates the entry field."""
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
