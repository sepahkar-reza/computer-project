import tkinter as tk
import random
import time
from threading import Thread


def roll_dice():
    def animate():
        for _ in range(10):  
            num = random.randint(1, 6)
            dice_label.config(text=str(num), font=("Arial", 60, "bold"))
            root.update()
            time.sleep(0.1)
        
        final_num = random.randint(1, 6)
        dice_label.config(text=str(final_num), font=("Arial", 80, "bold"))

    Thread(target=animate).start()


root = tk.Tk()
root.title("🎲 Dice Roller")
root.geometry("300x300")
root.config(bg="black")

dice_label = tk.Label(root, text="🎲", font=("Arial", 80), fg="lime", bg="black")
dice_label.pack(expand=True)

roll_button = tk.Button(root, text="Roll Dice!", command=roll_dice,
                        font=("Arial", 16, "bold"), bg="lime", fg="black")
roll_button.pack(pady=20)

root.mainloop()