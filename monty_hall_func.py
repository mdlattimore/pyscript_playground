from random import randint




def play():
    results = Element('results')

    try:
        number = int(Element('number').value)
    except:
        number = 0
        results.element.innerText = "Enter an integer"

    switch = True
    win = 0
    loss = 0
    if number > 0:
        if number > 1000000: number = 1000000
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

        results.element.innerText = f"""\
        Wins: {win}
        Losses: {loss}
        Win Percentage: {(win/number) * 100:.3f} %

        """