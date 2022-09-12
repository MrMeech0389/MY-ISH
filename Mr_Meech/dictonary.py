import random

user = input("rock paper or scissors?")

beats = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

choices = ["rock", "paper", "scissors"]

cpu = random.choice(choices)
print(f"cpu has selected: {cpu}")

if user == cpu:
    print("tie")
elif beats[user] == cpu:
    print("You Win!")
else:
    print("You Lose!")