import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# Colors and Fonts
BG_COLOR = "#2C3E50"  # Dark Background
BUTTON_COLOR = "#3498DB"  # Blue Buttons
BUTTON_HOVER = "#2980B9"  # Darker Blue
FONT_STYLE = ("Arial", 14)
TEXT_COLOR = "white"

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x450")
        self.root.configure(bg=BG_COLOR)

        # Title Label
        self.label = tk.Label(root, text="🔒 Password Generator", font=("Arial", 18, "bold"), fg=TEXT_COLOR, bg=BG_COLOR)
        self.label.pack(pady=10)

        # Length Input
        self.length_label = tk.Label(root, text="Enter Password Length:", font=FONT_STYLE, fg=TEXT_COLOR, bg=BG_COLOR)
        self.length_label.pack(pady=5)
        self.length_entry = tk.Entry(root, font=FONT_STYLE, width=10)
        self.length_entry.pack(pady=5)

        # Generate Button
        self.generate_button = self.create_button("🔄 Generate Password", self.generate_password)
        
        # Display Password
        self.password_entry = tk.Entry(root, font=FONT_STYLE, width=30, state="readonly")
        self.password_entry.pack(pady=5)

        # Password Strength Label
        self.strength_label = tk.Label(root, text="", font=("Arial", 12, "bold"), fg=TEXT_COLOR, bg=BG_COLOR)
        self.strength_label.pack(pady=5)

        # Copy Button
        self.copy_button = self.create_button("📋 Copy Password", self.copy_password)

    def create_button(self, text, command):
        """Creates a styled button with hover effect."""
        btn = tk.Button(self.root, text=text, font=FONT_STYLE, bg=BUTTON_COLOR, fg=TEXT_COLOR,
                        width=20, command=command)
        btn.pack(pady=5)
        btn.bind("<Enter>", lambda e: btn.config(bg=BUTTON_HOVER))
        btn.bind("<Leave>", lambda e: btn.config(bg=BUTTON_COLOR))
        return btn

    def generate_password(self):
        """Generate a random password and check its strength."""
        try:
            length = int(self.length_entry.get())
            if length < 4:
                messagebox.showwarning("Warning", "Password length should be at least 4!")
                return
            
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            
            self.password_entry.config(state="normal")
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password)
            self.password_entry.config(state="readonly")

            # Check Password Strength
            self.check_strength(password)

        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid number!")

    def check_strength(self, password):
        """Check the strength of the generated password."""
        length = len(password)
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in string.punctuation for c in password)

        strength = "Weak"
        color = "red"

        if length >= 8 and has_lower and has_upper and has_digit:
            strength = "Medium"
            color = "orange"
        if length >= 12 and has_lower and has_upper and has_digit and has_special:
            strength = "Strong"
            color = "green"

        self.strength_label.config(text=f"Strength: {strength}", fg=color)

    def copy_password(self):
        """Copy generated password to clipboard."""
        password = self.password_entry.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
