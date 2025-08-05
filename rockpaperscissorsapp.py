import tkinter as tk
import random
root = tk.Tk()
root.title("rock paper scissors")
root.geometry("250x200")
choices = ["rock", "paper", "scissors"]
result = tk.Label(root, text="", font=("arial", 12))
result.pack(pady=20)
def play(user_choice):
    computer = random.choice(choices)
    if user_choice == computer:
        outcome = "Draw!"
    elif (user_choice == "rock" and computer == "scissors") or \
         (user_choice == "paper" and computer == "rock") or \
         (user_choice == "scissors" and computer =="paper"):
        outcome = "you win"
    else:
        outcome = "computer wins"
        result.config(text=f"you: {user_choice}\ncomputer: {computer}\n{outcome}")
tk.Button(root, text="rock", width=10, command=lambda: play("rock")).pack(pady=5)
tk.Button(root, text="paper", width=10, command=lambda: play("paper")).pack(pady=5)
tk.button(root, text="scissors", width=10, command=lambda: play("scissors")).pack(pady=5)
root.mainloop()