# monty_hall_mark.py
"""My attempt at a Monty Hall Problem Simulation. 
Written before looking at Al Sweiger's. This is an 
automated version that runs 'n' simulations."""

from random import randint
import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system('clear')

clear()

print(" Monty Hall Problem ".center(80, "*"))
print()
print("""This is a program that simulates the classic "Monty Hall Problem" based
on the classic TV gameshow. In the show's gameplay, the host (Monty Hall) offers
the contestant a choice of three doors. Behind each door is a prize. Behind one 
door is the desirable prize (e.g. a new car). Behind the other two are worthless
prizes (often referred to in this problem as "goats"). When the contestant chooses
a door, Monty Hall (knowing where the car is), opens one of the doors hiding a goat,
leaving one door hiding a car, the other another goat. He then gives the contestant 
the opportunity either to switch their choice to the remaining door not picked, or 
to remain with their original choice. The question is this: is it better for the
contestant to switch their choice or to remain with their original choice? Intuitively,
it seems that it doesn't matter -- there are two doors remaining, one hiding a car,
the other hiding a goat, making either door equally likely to be hiding the car.
However, it is actually in the contestant's best interest to change their guess as
they have a 2/3 chance of winning if they do so. For a more detailed explanation as to
why switching is the better decision, see https://en.wikipedia.org/wiki/Monty_Hall_problem.

This simulator allows you to run mulitple simulations and see the results. The program
randomly selects a door hiding the car and then randomly selects the contestant's first
guess. One of the "goat" doors is eliminated and then the program either changes the
initial choice or remains with it. At the beginning of each simulation, the user decides
how many times to run the simulation and whether to stay with the original choice or
switch doors after the first is eliminated. The program either switches or stays 
every instance of the simulation.
""")

number = int(input("How many times would you like to run the simulation? "))

switch_choice = input("Do you want to switch the choice (y/n)? ")

clear()

win = 0
loss = 0

for _ in range(number):
    choices = [1, 2, 3]
    car = choices.pop(randint(0, 2))
    goats = choices
    selection = randint(1, 3)

    if selection == car:
        switch = switch_choice
        if switch.lower() == "y":
            # print("You lose.")
            loss += 1
        else:
            # print("You win!")
            win += 1

    elif selection != car:
        switch = switch_choice
        if switch.lower() == "y":
            # print("You win!")
            win += 1
        else:
            # print("You lose!")
            loss += 1

print()
print(f"Number of simulations: {number:,}")
print(f"Switch choice: {switch_choice}")
print(f"Wins:\t{win}")
print(f"Losses:\t{loss}")
print(f"Winning percentage: {(win / (win + loss)) * 100}%")
print()





