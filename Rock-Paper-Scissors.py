import tkinter as tk
from random import choice
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x400")
user_choice = tk.StringVar()
computer_choice = tk.StringVar()
result = tk.StringVar()
user_score = tk.IntVar()
computer_score = tk.IntVar()
def determine_winner(user_choice):
    choices = ['rock', 'paper', 'scissors']
    comp_choice = choice(choices)
    computer_choice.set(comp_choice)
    if user_choice == comp_choice:
        result.set("It's a tie!")
    elif (user_choice == 'rock' and comp_choice == 'scissors') or \
            (user_choice == 'scissors' and comp_choice == 'paper') or \
            (user_choice == 'paper' and comp_choice == 'rock'):
        result.set("You win!")
        user_score.set(user_score.get() + 1)
    else:
        result.set("Computer wins!")
        computer_score.set(computer_score.get() + 1)
def on_choice(choice):
    user_choice.set(choice)
    determine_winner(choice)
def play_again():
    user_choice.set("")
    computer_choice.set("")
    result.set("")
tk.Label(root, text="Choose Rock, Paper, or Scissors").pack(pady=10)
tk.Label(root, text="Your choice:").pack()
tk.Label(root, textvariable=user_choice).pack()
tk.Label(root, text="Computer's choice:").pack()
tk.Label(root, textvariable=computer_choice).pack()
tk.Label(root, textvariable=result, font=("Helvetica", 14)).pack(pady=10)
tk.Button(root, text="Rock", command=lambda: on_choice('rock')).pack(side=tk.LEFT, padx=10)
tk.Button(root, text="Paper", command=lambda: on_choice('paper')).pack(side=tk.LEFT, padx=10)
tk.Button(root, text="Scissors", command=lambda: on_choice('scissors')).pack(side=tk.LEFT, padx=10)
tk.Button(root, text="Play Again", command=play_again).pack(pady=20)
tk.Label(root, text="Your Score:").pack()
tk.Label(root, textvariable=user_score).pack()
tk.Label(root, text="Computer Score:").pack()
tk.Label(root, textvariable=computer_score).pack()
root.mainloop()