import tkinter as tk
import random

# Step 2: Initialize the game window with appropriate dimensions and title[span_0](start_span)[span_0](end_span)
root = tk.Tk()
root.title("HandCombat.Py")
root.geometry("400x400")

# Step 3: Set the background color of the window[span_2](start_span)[span_2](end_span)
root.configure(bg="#f0f0f0")

# Step 4: Create a label for the game title and display it[span_3](start_span)[span_3](end_span)
title_label = tk.Label(root, text="HandCombat", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#333333")
title_label.pack(pady=15)

# Step 5: Prompt the user to choose between rock, paper, or scissors[span_4](start_span)[span_4](end_span)
prompt_label = tk.Label(root, text="Choose rock, paper, or scissors:", font=("Helvetica", 12), bg="#f0f0f0")
prompt_label.pack(pady=5)

# Step 6: Create an input field for the user to enter their choice[span_5](start_span)[span_5](end_span)
user_entry = tk.Entry(root, font=("Helvetica", 12), justify="center")
user_entry.pack(pady=5)

# Label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 11), bg="#f0f0f0", justify="center")
result_label.pack(pady=15)

def play_game():
    user_choice = user_entry.get().strip().lower()
    choices = ["rock", "paper", "scissors"]

    if user_choice not in choices:
        result_label.config(text="Invalid choice! Please enter 'rock', 'paper', or 'scissors'.", fg="red")
        return

    # Step 7 & 8: Generate a random selection for the computer and assign it to comp_pick[span_6](start_span)[span_6](end_span)
    comp_pick = random.choice(choices)

    # Determine game outcome
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

# Play Button
play_button = tk.Button(root, text="Play", font=("Helvetica", 12, "bold"), command=play_game)
play_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()

