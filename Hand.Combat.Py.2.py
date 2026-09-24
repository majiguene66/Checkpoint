import tkinter as tk
import random

# Initialize main window
root = tk.Tk()
root.title("HandCombat.Py")
root.geometry("400x450")
root.configure(bg="#f0f0f0")

# Title Label
title_label = tk.Label(root, text="HandCombat", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#333333")
title_label.pack(pady=15)

# Input Prompt & Entry
prompt_label = tk.Label(root, text="Choose rock, paper, or scissors:", font=("Helvetica", 12), bg="#f0f0f0")
prompt_label.pack(pady=5)

user_entry = tk.Entry(root, font=("Helvetica", 12), justify="center")
user_entry.pack(pady=5)

# Result Output Label
result_label = tk.Label(root, text="", font=("Helvetica", 11), bg="#f0f0f0", justify="center")
result_label.pack(pady=15)

# Step 1 & 2: Define play() to handle game logic and conditional statements to determine the winner
def play():
    user_choice = user_entry.get().strip().lower()
    choices = ["rock", "paper", "scissors"]

    if user_choice not in choices:
        result_label.config(text="Invalid choice!\nPlease enter rock, paper, or scissors.", fg="red")
        return

    comp_pick = random.choice(choices)

    if user_choice == comp_pick:
        outcome = "It's a tie!"
    elif (user_choice == "rock" and comp_pick == "scissors") or \
         (user_choice == "paper" and comp_pick == "rock") or \
         (user_choice == "scissors" and comp_pick == "paper"):
        outcome = "You win!"
    else:
        outcome = "Computer wins!"

    result_label.config(
        text=f"Your choice: {user_choice.capitalize()}\n"
             f"Computer's choice: {comp_pick.capitalize()}\n\n"
             f"{outcome}",
        fg="black"
    )

# Step 3: Define Reset() to clear input and results
def Reset():
    user_entry.delete(0, tk.END)
    result_label.config(text="", fg="black")

# Step 4: Define Exit() to close the application
def Exit():
    root.destroy()

# Buttons Frame
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

play_btn = tk.Button(button_frame, text="PLAY", font=("Helvetica", 10, "bold"), width=8, command=play)
play_btn.grid(row=0, column=0, padx=5)

reset_btn = tk.Button(button_frame, text="RESET", font=("Helvetica", 10, "bold"), width=8, command=Reset)
reset_btn.grid(row=0, column=1, padx=5)

exit_btn = tk.Button(button_frame, text="EXIT", font=("Helvetica", 10, "bold"), width=8, command=Exit)
exit_btn.grid(row=0, column=2, padx=5)

root.mainloop()
