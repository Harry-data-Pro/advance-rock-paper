import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game 🎯")
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(root, text="Guess the number (1 to 100):")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.button = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.button.pack(pady=5)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

        self.restart_button = tk.Button(root, text="Play Again", command=self.restart_game)
        self.restart_button.pack(pady=5)
        self.restart_button.config(state="disabled")

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.number_to_guess:
                self.result_label.config(text="Too low!")
            elif guess > self.number_to_guess:
                self.result_label.config(text="Too high!")
            else:
                self.result_label.config(
                    text=f"🎉 Correct! You guessed it in {self.attempts} tries."
                )
                self.button.config(state="disabled")
                self.restart_button.config(state="normal")
        except ValueError:
            self.result_label.config(text="⚠️ Please enter a valid number.")

    def restart_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.button.config(state="normal")
        self.restart_button.config(state="disabled")

# Run the game
root = tk.Tk()
game = NumberGuessingGame(root)
root.mainloop()
