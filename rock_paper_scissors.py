import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")
        self.player_score = 0
        self.computer_score = 0
        self.choices = ['Rock', 'Paper', 'Scissors']
        self.create_widgets()

    def create_widgets(self):
        self.label_title = tk.Label(self.root, text="Rock, Paper, Scissors", font=("Arial", 16, "bold"))
        self.label_title.pack(pady=10)

        self.frame_buttons = tk.Frame(self.root)
        self.frame_buttons.pack(pady=10)
        for choice in self.choices:
            btn = tk.Button(self.frame_buttons, text=choice, width=10, font=("Arial", 12), command=lambda c=choice: self.play(c))
            btn.pack(side=tk.LEFT, padx=5)

        self.label_player = tk.Label(self.root, text="Your Choice: -", font=("Arial", 12))
        self.label_player.pack(pady=5)
        self.label_computer = tk.Label(self.root, text="Computer Choice: -", font=("Arial", 12))
        self.label_computer.pack(pady=5)
        self.label_result = tk.Label(self.root, text="Result: -", font=("Arial", 12, "bold"))
        self.label_result.pack(pady=10)
        self.label_score = tk.Label(self.root, text="Score - You: 0  Computer: 0", font=("Arial", 12))
        self.label_score.pack(pady=5)

    def play(self, player_choice):
        computer_choice = random.choice(self.choices)
        self.label_player.config(text=f"Your Choice: {player_choice}")
        self.label_computer.config(text=f"Computer Choice: {computer_choice}")
        result = self.get_result(player_choice, computer_choice)
        self.label_result.config(text=f"Result: {result}")
        self.label_score.config(text=f"Score - You: {self.player_score}  Computer: {self.computer_score}")

    def get_result(self, player, computer):
        if player == computer:
            return "Draw"
        elif (player == 'Rock' and computer == 'Scissors') or \
             (player == 'Paper' and computer == 'Rock') or \
             (player == 'Scissors' and computer == 'Paper'):
            self.player_score += 1
            return "You Win"
        else:
            self.computer_score += 1
            return "Computer Wins"

def main():
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()

if __name__ == "__main__":
    main()
