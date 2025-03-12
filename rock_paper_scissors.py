import tkinter as tk
import random

# Colors and Fonts
BG_COLOR = "#34495E"  # Dark Blue
BUTTON_COLOR = "#E74C3C"  # Red Buttons
BUTTON_HOVER = "#C0392B"  # Darker Red
FONT_STYLE = ("Arial", 14)
TEXT_COLOR = "white"

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("400x400")
        self.root.configure(bg=BG_COLOR)

        self.choices = ["Rock", "Paper", "Scissors"]
        self.user_score = 0
        self.computer_score = 0

        # Title
        self.label = tk.Label(root, text="🎮 Rock Paper Scissors", font=("Arial", 18, "bold"), fg=TEXT_COLOR, bg=BG_COLOR)
        self.label.pack(pady=10)

        # Buttons
        self.rock_button = self.create_button("🪨 Rock", "Rock")
        self.paper_button = self.create_button("📄 Paper", "Paper")
        self.scissors_button = self.create_button("✂ Scissors", "Scissors")

        # Result Label
        self.result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg=TEXT_COLOR, bg=BG_COLOR)
        self.result_label.pack(pady=10)

        # Score Label
        self.score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12, "bold"), fg=TEXT_COLOR, bg=BG_COLOR)
        self.score_label.pack(pady=5)

    def create_button(self, text, choice):
        """Creates a styled button with hover and click animation."""
        btn = tk.Button(self.root, text=text, font=FONT_STYLE, bg=BUTTON_COLOR, fg=TEXT_COLOR,
                        width=12, height=2, command=lambda: self.animate_button(btn, choice))
        btn.pack(pady=5)
        btn.bind("<Enter>", lambda e: btn.config(bg=BUTTON_HOVER))
        btn.bind("<Leave>", lambda e: btn.config(bg=BUTTON_COLOR))
        return btn

    def animate_button(self, button, user_choice):
        """Button animation effect when clicked."""
        button.config(bg="yellow")  # Change color when clicked
        self.root.after(200, lambda: button.config(bg=BUTTON_COLOR))  # Reset after 200ms
        self.play(user_choice)

    def play(self, user_choice):
        """Determines the winner and updates the score with animations."""
        computer_choice = random.choice(self.choices)

        if user_choice == computer_choice:
            result_text = f"It's a Tie! Both chose {user_choice}."
            result_color = "white"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Scissors" and computer_choice == "Paper") or \
             (user_choice == "Paper" and computer_choice == "Rock"):
            self.user_score += 1
            result_text = f"You Win! {user_choice} beats {computer_choice}."
            result_color = "green"
        else:
            self.computer_score += 1
            result_text = f"You Lose! {computer_choice} beats {user_choice}."
            result_color = "red"

        # Animate Result Text
        self.result_label.config(text="", fg=TEXT_COLOR)  # Reset text
        self.root.after(100, lambda: self.result_label.config(text=result_text, fg=result_color))

        # Animate Score Label
        self.score_label.config(text=f"Score - You: {self.user_score} | Computer: {self.computer_score}")
        self.root.after(200, lambda: self.score_label.config(fg=result_color))  # Change color for 200ms
        self.root.after(400, lambda: self.score_label.config(fg=TEXT_COLOR))  # Reset color

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()

