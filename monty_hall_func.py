from random import randint



def play():
    number = int(Element('number').value)
    switch = True
    win = 0
    loss = 0
    for _ in range(number):
        choices = [1, 2, 3]
        car = choices.pop(randint(0, 2))
        goats = choices
        selection = randint(1, 3)

        if selection == car:
            if switch:
                # print("You lose.")
                loss += 1
            else:
                # print("You win!")
                win += 1

        elif selection != car:
            if switch:
                # print("You win!")
                win += 1
            else:
                # print("You lose!")
                loss += 1

    results = Element('results')
    results.element.innerText = f"""\
    Wins: {win}
    Losses: {loss}
    Win Percentage: {(win/number) * 100:.3f} %

    """