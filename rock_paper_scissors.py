import time
import random

MOVES = ["rock", "paper", "scissors"]
WIN_MSG = ["You win!", "You dropped the bomb on me! You win!", "Grrrr... You win. Jerk."]
LOSE_MSG = ["Ha ha! You lose!", "Don't bring that weak game in here! You lose!", "You might be good. But I'm better! Non-winner"]
TIE_MSG = ["Great minds think alike. We tied.", "I see the way you think. We tied.", "No joy! Tie."]

def play(move):
    computer_move = random.choice(MOVES)
    print(f"Your move: {move}")
    print(f"Computer's move: {computer_move}")
    print()
    if move.lower() == "rock":
        if computer_move == "rock":
            print(random.choice(TIE_MSG))
        elif computer_move == "scissors":
            print(random.choice(WIN_MSG))
        else:
            print(random.choice(LOSE_MSG))
    elif move.lower() == "paper":
        if computer_move == "paper":
            print(random.choice(TIE_MSG))
        elif computer_move == "rock":
            print(random.choice(WIN_MSG))
        else:
            print(random.choice(LOSE_MSG))
    else:
        if computer_move == "scissors":
            print(andom.choice(TIE_MSG))
        elif computer_move == "paper":
            print(random.choice(WIN_MSG))
        else:
            print(random.choice(LOSE_MSG))
    print()
    
while True:
    print()
    user_move = input("What's your move? ")
    if user_move.lower() == "quit" or user_move.lower() == "q":
        print()
        print("Thanks for playing!")
        print()
        break
    elif user_move.lower() not in MOVES:
        print("Invalid guess, try again! ")
        print()
        continue
    else:
        print()
        print("Rock", end="...", flush=True)
        time.sleep(.5)
        print("Paper", end="...", flush=True)
        time.sleep(.5)
        print("Scissors", end="...", flush=True)
        time.sleep(.5)
        print("Shoot!")
        print()
    play(user_move)