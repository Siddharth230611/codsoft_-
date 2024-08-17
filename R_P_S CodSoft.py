
import tkinter as tk
import random

def winner(player_choice):
    choices = ["Rock", "Paper", "Scissor"]
    computer_choice = random.choice(choices)
    if player_choice == computer_choice:
        return computer_choice, "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissor") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissor" and computer_choice == "Paper"):
        return computer_choice, "You win!"
    else:
        return computer_choice, "You lose!"

def button_click(choice):
    computer_choice, result = winner(choice)
    result_text.set(f"Computer chose: {computer_choice}\n{result}")

root = tk.Tk()
root.title("Rock Paper Scissor")

tk.Label(root, text="Rock Paper Scissor", font=("Arial", 16)).pack(pady=10)

for choice in ["Rock", "Paper", "Scissor"]:
    tk.Button(root, text=choice, width=15, command=lambda c=choice: button_click(c)).pack(pady=5)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, font=("Arial", 12)).pack(pady=20)

root.mainloop()



