import random

# roll_list = []

def roll_dice():
    results = Element('results')
    global dice
    # global roll_list
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    # interleave dice[die1] and dice[die2] by index to display dice side by side. Use rstrip() to strip the newline character
    combined = f"""\
    {dice[die1][0:10].rstrip()}   {dice[die2][0:10].rstrip()}
    {dice[die1][10:20].rstrip()}   {dice[die2][10:20].rstrip()}
    {dice[die1][20:30].rstrip()}   {dice[die2][20:30].rstrip()}
    {dice[die1][30:40].rstrip()}   {dice[die2][30:40].rstrip()}
    {dice[die1][40:50].rstrip()}   {dice[die2][40:50].rstrip()}

    {str(die1 + die2).center(22)}"""
    # roll_list.append(die1 + die2)
    
    if die1 == 1 and die2 == 1:
        combined += "\n         SNAKE EYES!".center(30)
    elif die1 == die2:
        combined += "\n           DOUBLES!".center(30)
    else:
        combined += "\n\n"

    results.element.innerHTML = f"<pre>{combined}</pre>"

# Store ascii dice in dictionary
dice = {1: """\
---------
|       |
|   o   |
|       |
---------""",
2: """\
---------
|o      |
|       |
|      o|
---------""",
3: """\
---------
|o      |
|   o   |
|      o|
---------""",
4: """\
---------
|o     o|
|       |
|o     o|
---------""",
5: """\
---------
|o     o|
|   o   |
|o     o|
---------""",
6: """\
---------
|o     o|
|o     o|
|o     o|
---------"""}





    