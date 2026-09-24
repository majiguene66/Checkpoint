import tkinter as tk
import random

# Initialisation de la fenêtre principale
root = tk.Tk()
root.title("HandCombat.Py")
root.geometry("400x450")
root.configure(bg="#f0f0f0")

# Titre de l'application
title_label = tk.Label(root, text="HandCombat", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#333333")
title_label.pack(pady=15)

# Zone de saisie pour le choix de l'utilisateur
prompt_label = tk.Label(root, text="Choose rock, paper, or scissors:", font=("Helvetica", 12), bg="#f0f0f0")
prompt_label.pack(pady=5)

user_entry = tk.Entry(root, font=("Helvetica", 12), justify="center")
user_entry.pack(pady=5)

# Étape 1 : Création de la variable Result et du champ Entry pour afficher le résultat[span_1](start_span)[span_1](end_span)
Result = tk.StringVar()
result_entry = tk.Entry(root, textvariable=Result, font=("Helvetica", 11), width=35, justify="center")

# Logique du jeu : Fonction play()
def play():
    user_choice = user_entry.get().strip().lower()
    choices = ["rock", "paper", "scissors"]

    if user_choice not in choices:
        Result.set("Choix invalide ! Entrez rock, paper ou scissors.")
        return

    comp_pick = random.choice(choices)

    if user_choice == comp_pick:
        outcome = "Égalité !"
    elif (user_choice == "rock" and comp_pick == "scissors") or \
         (user_choice == "paper" and comp_pick == "rock") or \
         (user_choice == "scissors" and comp_pick == "paper"):
        outcome = "Vous avez gagné !"
    else:
        outcome = "L'ordinateur a gagné !"

    # Mise à jour de la variable Result[span_2](start_span)[span_2](end_span)
    Result.set(f"Joueur: {user_choice} | Ordi: {comp_pick} -> {outcome}")

# Étape 3 : Fonction Reset()[span_3](start_span)[span_3](end_span)
def Reset():
    user_entry.delete(0, tk.END)
    Result.set("")

# Étape 4 : Fonction Exit()[span_4](start_span)[span_4](end_span)
def Exit():
    root.destroy()

# Étape 2, 3, 4, 5 : Création et placement des boutons et du champ de résultat[span_5](start_span)[span_5](end_span)
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=15)

play_btn = tk.Button(button_frame, text="PLAY", font=("Helvetica", 10, "bold"), width=8, command=play)
play_btn.grid(row=0, column=0, padx=5)

reset_btn = tk.Button(button_frame, text="RESET", font=("Helvetica", 10, "bold"), width=8, command=Reset)
reset_btn.grid(row=0, column=1, padx=5)

exit_btn = tk.Button(button_frame, text="EXIT", font=("Helvetica", 10, "bold"), width=8, command=Exit)
exit_btn.grid(row=0, column=2, padx=5)

# Placement du champ de résultat[span_6](start_span)[span_6](end_span)
result_entry.pack(pady=15)

# Étape 6 : Lancement de l'application via root.mainloop()[span_7](start_span)[span_7](end_span)
root.mainloop()
