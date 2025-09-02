import tkinter as tk
from tkinter import messagebox
import random

class AdvancedNumberGuessingGame:
    def __init__(self, root):
        """
        Initialize the advanced GUI game with level system
        """
        self.root = root
        self.root.title("🎮 Advanced Number Guessing Game")
        self.root.geometry("600x700")
        self.root.configure(bg="#f0f0f0")
        
        # Game variables with level system
        self.level = 1
        self.score = 0
        self.max_level = 10
        self.secret_number = 0
        self.max_attempts = 0
        self.attempts = 0
        self.game_over = False
        
        # Level configuration
        self.level_config = {
            1: {"range": (1, 100), "attempts": 10},
            2: {"range": (1, 150), "attempts": 9},
            3: {"range": (1, 200), "attempts": 8},
            4: {"range": (1, 300), "attempts": 8},
            5: {"range": (1, 400), "attempts": 7},
            6: {"range": (1, 500), "attempts": 7},
            7: {"range": (1, 750), "attempts": 6},
            8: {"range": (1, 1000), "attempts": 6},
            9: {"range": (1, 1500), "attempts": 5},
            10: {"range": (1, 2000), "attempts": 5}
        }
        
        # Initialize first level
        self.start_new_level()
        
        # Create GUI elements
        self.create_widgets()
        
    def start_new_level(self):
        """
        شروع یک مرحله جدید با پیکربندی به‌روزشده
        """
        # این تابع یک مرحله جدید را با توجه به سطح فعلی آغاز می‌کند.
        # ابتدا تنظیمات مربوط به سطح فعلی (محدوده عدد و تعداد تلاش‌ها) را از دیکشنری سطح‌ها می‌گیرد.
        config = self.level_config[self.level]
        # یک عدد تصادفی جدید در محدوده تعیین‌شده برای این سطح انتخاب می‌کند.
        self.secret_number = random.randint(config["range"][0], config["range"][1])
        # تعداد تلاش‌های مجاز را برای این سطح تنظیم می‌کند.
        self.max_attempts = config["attempts"]
        # شمارنده تلاش‌ها را صفر می‌کند تا مرحله جدید شروع شود.
        self.attempts = 0
        # وضعیت پایان بازی را به False برمی‌گرداند تا بازی فعال شود.
        self.game_over = False
        
    def create_widgets(self):
        """
        Create all GUI widgets
        """
        # Main title
        title_label = tk.Label(
            self.root,
            text="🎮 Advanced Number Guessing Game",
            font=("Arial", 18, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        title_label.pack(pady=15)
        
        # Level and score display
        level_frame = tk.Frame(self.root, bg="#f0f0f0")
        level_frame.pack(pady=10)
        
        self.level_label = tk.Label(
            level_frame,
            text=f"Level: {self.level}/{self.max_level}",
            font=("Arial", 14, "bold"),
            bg="#f0f0f0",
            fg="#007acc"
        )
        self.level_label.pack(side=tk.LEFT, padx=10)
        
        self.score_label = tk.Label(
            level_frame,
            text=f"Score: {self.score}",
            font=("Arial", 14, "bold"),
            bg="#f0f0f0",
            fg="#28a745"
        )
        self.score_label.pack(side=tk.RIGHT, padx=10)
        
        # Level info
        config = self.level_config[self.level]
        self.level_info_label = tk.Label(
            self.root,
            text=f"Range: {config['range'][0]} - {config['range'][1]} | Max Attempts: {config['attempts']}",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#666666"
        )
        self.level_info_label.pack(pady=5)
        
        # Instructions
        instructions = tk.Label(
            self.root,
            text="Guess the number and advance to higher levels!\nEach level gets more challenging.",
            font=("Arial", 11),
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
            text="Enter your guess:",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#333333"
        )
        input_label.pack()
        
        # Input entry
        self.guess_entry = tk.Entry(
            input_frame,
            font=("Arial", 14),
            width=15,
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
            wraplength=550
        )
        self.result_label.pack(pady=20)
        
        # Hint display
        self.hint_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#666666",
            wraplength=550
        )
        self.hint_label.pack(pady=10)
        
        # Progress bar frame
        progress_frame = tk.Frame(self.root, bg="#f0f0f0")
        progress_frame.pack(pady=10)
        
        # Progress bar
        self.progress_label = tk.Label(
            progress_frame,
            text="Progress:",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#333333"
        )
        self.progress_label.pack()
        
        self.progress_bar = tk.Canvas(
            progress_frame,
            width=400,
            height=20,
            bg="#e0e0e0",
            highlightthickness=0
        )
        self.progress_bar.pack(pady=5)
        self.update_progress_bar()
        
    def update_progress_bar(self):
        """
        Update the progress bar based on current level
        """
        self.progress_bar.delete("all")
        progress = (self.level - 1) / self.max_level
        bar_width = int(400 * progress)
        
        # Draw progress bar
        self.progress_bar.create_rectangle(0, 0, 400, 20, fill="#e0e0e0", outline="")
        self.progress_bar.create_rectangle(0, 0, bar_width, 20, fill="#007acc", outline="")
        
        # Add text
        self.progress_bar.create_text(
            200, 10,
            text=f"Level {self.level} of {self.max_level}",
            font=("Arial", 10, "bold"),
            fill="#333333"
        )
        
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
        config = self.level_config[self.level]
        if guess < config["range"][0] or guess > config["range"][1]:
            messagebox.showerror("Invalid Range", f"Please enter a number between {config['range'][0]} and {config['range'][1]}!")
            self.guess_entry.delete(0, tk.END)
            return
            
        # Increment attempts
        self.attempts += 1
        
        # Check the guess
        if guess == self.secret_number:
            # User won the level
            level_score = self.max_attempts - self.attempts + 1
            self.score += level_score
            
            if self.level < self.max_level:
                # Advance to next level
                self.level += 1
                self.result_label.config(
                    text=f"🎉 Congratulations! You completed Level {self.level - 1}!\n✅ Correct number: {self.secret_number}\n🏆 Level score: +{level_score}\n📈 Advancing to Level {self.level}!",
                    fg="#28a745"
                )
                self.hint_label.config(text="")
                self.game_over = True
                self.submit_button.config(state="disabled")
                
                # Auto-start next level after 3 seconds
                self.root.after(3000, self.advance_to_next_level)
            else:
                # Game completed!
                self.result_label.config(
                    text=f"🏆 CONGRATULATIONS! You've completed all levels!\n🎉 Final Score: {self.score}\n🌟 You are a master number guesser!",
                    fg="#ffd700"
                )
                self.hint_label.config(text="")
                self.game_over = True
                self.submit_button.config(state="disabled")
            
        else:
            # Calculate the difference percentage for better hints
            config = self.level_config[self.level]
            range_size = config["range"][1] - config["range"][0] + 1
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
                        text=f"💡 Hint: The correct number is between {guess} and {self.level_config[self.level]['range'][1]}."
                    )
                else:
                    self.hint_label.config(
                        text=f"💡 Hint: The correct number is between {self.level_config[self.level]['range'][0]} and {guess}."
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
                text=f"😔 Sorry, you lost Level {self.level}!\n❌ The correct number was: {self.secret_number}\n🔄 Try again or start a new game!",
                fg="#dc3545"
            )
            self.hint_label.config(text="")
            self.game_over = True
            self.submit_button.config(state="disabled")
            
    def advance_to_next_level(self):
        """
        Advance to the next level
        """
        self.start_new_level()
        self.update_display()
        self.submit_button.config(state="normal")
        self.guess_entry.focus()
        
    def update_display(self):
        """
        Update all display elements
        """
        config = self.level_config[self.level]
        
        # Update level and score
        self.level_label.config(text=f"Level: {self.level}/{self.max_level}")
        self.score_label.config(text=f"Score: {self.score}")
        
        # Update level info
        self.level_info_label.config(text=f"Range: {config['range'][0]} - {config['range'][1]} | Max Attempts: {config['attempts']}")
        
        # Update attempts
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")
        self.remaining_label.config(text=f"Remaining: {self.max_attempts - self.attempts}")
        
        # Update progress bar
        self.update_progress_bar()
        
        # Clear result and hint
        self.result_label.config(text="")
        self.hint_label.config(text="")
            
    def new_game(self):
        """
        Start a new game
        """
        # Reset game variables
        self.level = 1
        self.score = 0
        self.start_new_level()
        self.update_display()
        self.submit_button.config(state="normal")
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()

def main():
    """
    Main function to run the advanced GUI game
    """
    root = tk.Tk()
    game = AdvancedNumberGuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main() 