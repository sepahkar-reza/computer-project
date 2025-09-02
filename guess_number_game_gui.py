import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        """
        Initialize the GUI game
        """
        self.root = root
        self.root.title("🎮 Number Guessing Game")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f0f0")
        
        # Game variables
        self.secret_number = random.randint(1, 100)
        self.max_attempts = 10
        self.attempts = 0
        self.game_over = False
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        """
        Create all GUI widgets
        """
        # Main title
        title_label = tk.Label(
            self.root,
            text="🎮 Number Guessing Game",
            font=("Arial", 20, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        title_label.pack(pady=20)
        
        # Instructions
        instructions = tk.Label(
            self.root,
            text="I have chosen a number between 1 and 100.\nYou have 10 attempts to guess it!",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#666666",
            justify="center"
        )
        instructions.pack(pady=10)
        
        # Attempts display
        self.attempts_label = tk.Label(
            self.root,
            text=f"Attempts: {self.attempts}/{self.max_attempts}",
            font=("Arial", 14, "bold"),
            bg="#f0f0f0",
            fg="#007acc"
        )
        self.attempts_label.pack(pady=10)
        
        # Remaining attempts
        self.remaining_label = tk.Label(
            self.root,
            text=f"Remaining: {self.max_attempts - self.attempts}",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#666666"
        )
        self.remaining_label.pack(pady=5)
        
        # Input frame
        input_frame = tk.Frame(self.root, bg="#f0f0f0")
        input_frame.pack(pady=20)
        
        # Input label
        input_label = tk.Label(
            input_frame,
            text="Enter your guess (1-100):",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#333333"
        )
        input_label.pack()
        
        # Input entry
        self.guess_entry = tk.Entry(
            input_frame,
            font=("Arial", 14),
            width=10,
            justify="center"
        )
        self.guess_entry.pack(pady=10)
        self.guess_entry.focus()
        
        # Bind Enter key to submit
        self.guess_entry.bind('<Return>', self.submit_guess)
        
        # Submit button
        self.submit_button = tk.Button(
            input_frame,
            text="Submit Guess",
            font=("Arial", 12, "bold"),
            bg="#007acc",
            fg="white",
            command=self.submit_guess,
            width=15,
            height=2
        )
        self.submit_button.pack(pady=10)
        
        # New game button
        self.new_game_button = tk.Button(
            input_frame,
            text="New Game",
            font=("Arial", 12, "bold"),
            bg="#28a745",
            fg="white",
            command=self.new_game,
            width=15,
            height=2
        )
        self.new_game_button.pack(pady=5)
        
        # Result display
        self.result_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 14),
            bg="#f0f0f0",
            fg="#333333",
            wraplength=450
        )
        self.result_label.pack(pady=20)
        
        # Hint display
        self.hint_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#666666",
            wraplength=450
        )
        self.hint_label.pack(pady=10)
        
    def submit_guess(self, event=None):
        """
        Handle guess submission
        """
        if self.game_over:
            return
            
        # Get user input
        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number!")
            self.guess_entry.delete(0, tk.END)
            return
            
        # Validate input range
        if guess < 1 or guess > 100:
            messagebox.showerror("Invalid Range", "Please enter a number between 1 and 100!")
            self.guess_entry.delete(0, tk.END)
            return
            
        # Increment attempts
        self.attempts += 1
        
        # Check the guess
        if guess == self.secret_number:
            # User won
            self.result_label.config(
                text=f"🎉 Congratulations! You won!\n✅ Correct number: {self.secret_number}\n🏆 Your attempts: {self.attempts}",
                fg="#28a745"
            )
            self.hint_label.config(text="")
            self.game_over = True
            self.submit_button.config(state="disabled")
            
        else:
            # Calculate the difference percentage for better hints
            range_size = 100  # 1 to 100
            difference = abs(guess - self.secret_number)
            difference_percentage = (difference / range_size) * 100
            
            if guess < self.secret_number:
                # Guess is too low
                if difference_percentage > 50:
                    hint_text = f"📈 Your guess ({guess}) is WAY TOO LOW! Guess much higher!"
                    hint_color = "#dc3545"  # Red for very far
                elif difference_percentage > 20:
                    hint_text = f"📈 Your guess ({guess}) is too low. Guess higher!"
                    hint_color = "#ffc107"  # Yellow for moderate
                else:
                    hint_text = f"📈 Your guess ({guess}) is slightly low. Guess a bit higher!"
                    hint_color = "#17a2b8"  # Blue for close
            else:
                # Guess is too high
                if difference_percentage > 50:
                    hint_text = f"📉 Your guess ({guess}) is WAY TOO HIGH! Guess much lower!"
                    hint_color = "#dc3545"  # Red for very far
                elif difference_percentage > 20:
                    hint_text = f"📉 Your guess ({guess}) is too high. Guess lower!"
                    hint_color = "#ffc107"  # Yellow for moderate
                else:
                    hint_text = f"📉 Your guess ({guess}) is slightly high. Guess a bit lower!"
                    hint_color = "#17a2b8"  # Blue for close
            
            self.result_label.config(text=hint_text, fg=hint_color)
            
            # Provide range hints
            if self.max_attempts - self.attempts > 0:
                if guess < self.secret_number:
                    self.hint_label.config(
                        text=f"💡 Hint: The correct number is between {guess} and 100."
                    )
                else:
                    self.hint_label.config(
                        text=f"💡 Hint: The correct number is between 1 and {guess}."
                    )
            else:
                self.hint_label.config(text="")
        
        # Update attempts display
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")
        self.remaining_label.config(text=f"Remaining: {self.max_attempts - self.attempts}")
        
        # Clear input
        self.guess_entry.delete(0, tk.END)
        
        # Check if game is over (no more attempts)
        if self.attempts >= self.max_attempts and not self.game_over:
            self.result_label.config(
                text=f"😔 Sorry, you lost!\n❌ The correct number was: {self.secret_number}",
                fg="#dc3545"
            )
            self.hint_label.config(text="")
            self.game_over = True
            self.submit_button.config(state="disabled")
            
    def new_game(self):
        """
        Start a new game
        """
        # Reset game variables
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.game_over = False
        
        # Reset GUI elements
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")
        self.remaining_label.config(text=f"Remaining: {self.max_attempts - self.attempts}")
        self.result_label.config(text="")
        self.hint_label.config(text="")
        self.submit_button.config(state="normal")
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()

def main():
    """
    Main function to run the GUI game
    """
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main() 