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
        """Creates a styled button with hover effect."""
        btn = tk.Button(self.root, text=text, font=FONT_STYLE, bg=BUTTON_COLOR, fg=TEXT_COLOR,
                        width=12, height=2, command=lambda: self.play(choice))
        btn.pack(pady=5)
        btn.bind("<Enter>", lambda e: btn.config(bg=BUTTON_HOVER))
        btn.bind("<Leave>", lambda e: btn.config(bg=BUTTON_COLOR))
        return btn

    def play(self, user_choice):
        """Determines the winner and updates the score."""
        computer_choice = random.choice(self.choices)

        if user_choice == computer_choice:
            result_text = f"It's a Tie! Both chose {user_choice}."
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Scissors" and computer_choice == "Paper") or \
             (user_choice == "Paper" and computer_choice == "Rock"):
            self.user_score += 1
            result_text = f"You Win! {user_choice} beats {computer_choice}."
        else:
            self.computer_score += 1
            result_text = f"You Lose! {computer_choice} beats {user_choice}."

        # Update Labels
        self.result_label.config(text=result_text)
        self.score_label.config(text=f"Score - You: {self.user_score} | Computer: {self.computer_score}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()
