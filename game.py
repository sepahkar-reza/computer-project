import tkinter as tk
import random
from playsound import playsound
import threading

def play(user_choice):
    options = ["سنگ", "کاغذ", "قیچی"]
    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        result = "مساوی!"
        color = "orange"
        threading.Thread(target=lambda: playsound('draw.mp3')).start()
    elif (user_choice == "سنگ" and computer_choice == "قیچی") or \
         (user_choice == "قیچی" and computer_choice == "کاغذ") or \
         (user_choice == "کاغذ" and computer_choice == "سنگ"):
        result = "شما بردید!"
        color = "green"
        threading.Thread(target=lambda: playsound('win.mp3')).start()
    else:
        result = "کامپیوتر برد!"
        color = "red"
        threading.Thread(target=lambda: playsound('lose.mp3')).start()

    result_label.config(text=f"شما: {user_choice}\nکامپیوتر: {computer_choice}\nنتیجه: {result}")
    animate_result(color)

def animate_result(color):
    
    def flash(count):
        if count > 0:
            current = result_label.cget("fg")
            next_color = color if current != color else "black"
            result_label.config(fg=next_color)
            window.after(200, flash, count-1)
        else:
            result_label.config(fg=color)
    flash(6)


window = tk.Tk()
window.title("🎮 بازی سنگ کاغذ قیچی 🎮")
window.geometry("400x400")
window.configure(bg="#f0f0f0")


title_label = tk.Label(window, text="یک گزینه انتخاب کنید:", font=("Vazir", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=20)


button_frame = tk.Frame(window, bg="#f0f0f0")
button_frame.pack()

rock_button = tk.Button(button_frame, text="🪨 سنگ", width=12, height=2, bg="#ffcccb", font=("Vazir", 12, "bold"), command=lambda: play("سنگ"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="📄 کاغذ", width=12, height=2, bg="#d1e7dd", font=("Vazir", 12, "bold"), command=lambda: play("کاغذ"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="✂️ قیچی", width=12, height=2, bg="#cfe2ff", font=("Vazir", 12, "bold"), command=lambda: play("قیچی"))
scissors_button.grid(row=0, column=2, padx=10)


result_label = tk.Label(window, text="", font=("Vazir", 14, "bold"), bg="#f0f0f0")
result_label.pack(pady=30)

window.mainloop()