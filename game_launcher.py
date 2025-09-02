import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

class GameLauncher:
    def __init__(self, root):
        """
        Initialize the main game launcher
        """
        self.root = root
        self.root.title("🎮 Game Center - مرکز بازی‌ها")
        self.root.geometry("800x600")
        self.root.configure(bg="#2c3e50")
        
        # User name
        self.user_name = ""
        self.current_screen = "login"
        # Keep references to child Toplevel windows to prevent garbage collection
        self.child_windows = []
        # Status label reference (set in menu screen)
        self.status_label = None
        
        # Create GUI elements
        self.create_login_screen()
        
    def create_login_screen(self):
        """
        Create the login screen with name input
        """
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()
        # Reset window size for login screen
        try:
            self.root.state("normal")
        except Exception:
            pass
        self.root.geometry("800x600")
            
        # Main title
        title_label = tk.Label(
            self.root,
            text="🎮 Game Center",
            font=("Arial", 32, "bold"),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        title_label.pack(pady=50)
        
        subtitle_label = tk.Label(
            self.root,
            text="مرکز بازی‌ها",
            font=("Arial", 18),
            bg="#2c3e50",
            fg="#bdc3c7"
        )
        subtitle_label.pack(pady=10)
        
        # Login frame
        login_frame = tk.Frame(self.root, bg="#2c3e50")
        login_frame.pack(pady=50)
        
        # Name label
        name_label = tk.Label(
            login_frame,
            text="لطفاً نام خود را وارد کنید:",
            font=("Arial", 14),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        name_label.pack(pady=10)
        
        # Name entry
        self.name_entry = tk.Entry(
            login_frame,
            font=("Arial", 16),
            width=25,
            justify="center",
            bg="#34495e",
            fg="#ecf0f1",
            insertbackground="#ecf0f1"
        )
        self.name_entry.pack(pady=20)
        self.name_entry.focus()
        
        # Bind Enter key to start
        self.name_entry.bind('<Return>', self.start_game)
        
        # Start button
        start_button = tk.Button(
            login_frame,
            text="شروع",
            font=("Arial", 16, "bold"),
            bg="#27ae60",
            fg="white",
            command=self.start_game,
            width=15,
            height=2,
            relief="flat",
            cursor="hand2"
        )
        start_button.pack(pady=20)
        
    def start_game(self, event=None):
        """
        Start the game and show welcome message
        """
        self.user_name = self.name_entry.get().strip()
        
        if not self.user_name:
            messagebox.showerror("خطا", "لطفاً نام خود را وارد کنید!")
            return
            
        # Show welcome message
        messagebox.showinfo("خوش آمدید", f"سلام {self.user_name}! به مرکز بازی‌ها خوش آمدید!")
        
        # Switch to game menu
        self.show_game_menu()
        
    def show_game_menu(self):
        """
        Show the game selection menu
        """
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()
        # Enlarge/maximize window for games grid
        try:
            self.root.state("zoomed")
        except Exception:
            self.root.geometry("1280x800")
            
        # Header
        header_frame = tk.Frame(self.root, bg="#2c3e50")
        header_frame.pack(fill="x", pady=20)
        
        welcome_label = tk.Label(
            header_frame,
            text=f"خوش آمدید {self.user_name}!",
            font=("Arial", 20, "bold"),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        welcome_label.pack()
        
        subtitle_label = tk.Label(
            header_frame,
            text="بازی مورد نظر خود را انتخاب کنید:",
            font=("Arial", 14),
            bg="#2c3e50",
            fg="#bdc3c7"
        )
        subtitle_label.pack(pady=10)
        self.status_label = subtitle_label
        
        # Games container
        games_frame = tk.Frame(self.root, bg="#2c3e50")
        games_frame.pack(expand=True, fill="both", padx=50, pady=30)
        
        # Configure grid
        games_frame.grid_columnconfigure(0, weight=1)
        games_frame.grid_columnconfigure(1, weight=1)
        games_frame.grid_columnconfigure(2, weight=1)
        
        # Game 1: Number Guessing Game (Advanced)
        self.create_game_card(
            games_frame, 
            0, 0,
            "🔢 بازی حدس عدد پیشرفته",
            "بازی حدس عدد با سیستم سطح‌بندی و 10 سطح مختلف",
            "#3498db",
            self.launch_advanced_number_game
        )
        
        # Game 2: Number Guessing Game (Basic)
        self.create_game_card(
            games_frame, 
            0, 1,
            "🎯 بازی حدس عدد ساده",
            "بازی حدس عدد ساده با رابط گرافیکی",
            "#e74c3c",
            self.launch_basic_number_game
        )
        
        # Game 3: Rock Paper Scissors
        self.create_game_card(
            games_frame, 
            0, 2,
            "✂️ سنگ کاغذ قیچی",
            "بازی کلاسیک با انیمیشن و صدا (اختیاری)",
            "#8e44ad",
            self.launch_rock_paper_scissors
        )
        
        # Back button
        back_button = tk.Button(
            self.root,
            text="بازگشت به صفحه ورود",
            font=("Arial", 12),
            bg="#95a5a6",
            fg="white",
            command=self.create_login_screen,
            relief="flat",
            cursor="hand2"
        )
        back_button.pack(pady=20)
        
    def create_game_card(self, parent, row, col, title, description, color, command):
        """
        Create a game card with icon and description
        """
        # Card frame
        card_frame = tk.Frame(
            parent,
            bg=color,
            relief="raised",
            bd=1,
            cursor="hand2"
        )
        card_frame.grid(row=row, column=col, padx=8, pady=8, sticky="nsew")
        card_frame.bind("<Button-1>", lambda e: command())
        
        # Title
        title_label = tk.Label(
            card_frame,
            text=title,
            font=("Arial", 14, "bold"),
            bg=color,
            fg="white",
            wraplength=180
        )
        title_label.pack(pady=12)
        
        # Description
        desc_label = tk.Label(
            card_frame,
            text=description,
            font=("Arial", 11),
            bg=color,
            fg="white",
            wraplength=180,
            justify="center"
        )
        desc_label.pack(pady=8, padx=14)
        
        # Play button
        play_button = tk.Button(
            card_frame,
            text="شروع بازی",
            font=("Arial", 11, "bold"),
            bg="white",
            fg=color,
            command=command,
            relief="flat",
            cursor="hand2"
        )
        play_button.pack(pady=12)
        
    def launch_advanced_number_game(self):
        """
        Launch the advanced number guessing game
        """
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            script_path = os.path.join(script_dir, "guess_number_game_gui_advanced.py")
            creationflags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
            subprocess.Popen([sys.executable, script_path], cwd=script_dir, creationflags=creationflags)
            self._show_status_temporarily("در حال راه‌اندازی بازی حدس عدد پیشرفته…")
        except Exception as e:
            messagebox.showerror("خطا", f"خطا در راه‌اندازی بازی: {str(e)}")
            
    def launch_basic_number_game(self):
        """
        Launch the basic number guessing game
        """
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            script_path = os.path.join(script_dir, "guess_number_game_gui.py")
            creationflags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
            subprocess.Popen([sys.executable, script_path], cwd=script_dir, creationflags=creationflags)
            self._show_status_temporarily("در حال راه‌اندازی بازی حدس عدد ساده…")
        except Exception as e:
            messagebox.showerror("خطا", f"خطا در راه‌اندازی بازی: {str(e)}")
            
    def launch_rock_paper_scissors(self):
        """
        Launch the Rock-Paper-Scissors game
        """
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            if script_dir not in sys.path:
                sys.path.insert(0, script_dir)
            import importlib
            try:
                rps_module = importlib.import_module("rock_paper_scissors")
                if hasattr(rps_module, "open_in_toplevel"):
                    top = rps_module.open_in_toplevel(self.root)
                    # Keep a reference and bring to front
                    self.child_windows.append(top)
                    try:
                        top.transient(self.root)
                        top.deiconify()
                        top.lift()
                        top.focus_force()
                        top.attributes('-topmost', True)
                        self.root.after(300, lambda: top.attributes('-topmost', False))
                    except Exception:
                        pass
                    self._show_status_temporarily("بازی سنگ کاغذ قیچی باز شد.")
                    return
            except Exception:
                # Will fallback below
                pass

            # Fallback: run as a separate process to ensure it opens
            script_path = os.path.join(script_dir, "rock_paper_scissors.py")
            creationflags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
            subprocess.Popen([sys.executable, script_path], cwd=script_dir, creationflags=creationflags)
            self._show_status_temporarily("در حال راه‌اندازی سنگ کاغذ قیچی…")
        except Exception as e:
            messagebox.showerror("خطا", f"خطا در راه‌اندازی سنگ کاغذ قیچی: {str(e)}")

    def _show_status_temporarily(self, text: str, ms: int = 1500) -> None:
        try:
            if self.status_label is not None:
                self.status_label.config(text=text)
                self.root.after(ms, lambda: self.status_label and self.status_label.config(text="بازی مورد نظر خود را انتخاب کنید:"))
        except Exception:
            pass

def main():
    """
    Main function to run the game launcher
    """
    root = tk.Tk()
    app = GameLauncher(root)
    root.mainloop()

if __name__ == "__main__":
    main() 