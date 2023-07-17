import time


def collatz():
    num = int(Element('number').value)
    results = Element('results')
    output = ""
    output += f"Number: {num}\n" 
    steps = 0
    start = time.perf_counter()
    while num > 1:
        if num == 1:
            output += str(num)
            steps += 1
            break
        elif num % 2 == 0:
            num = num // 2
            if num == 1:
                output += str(num) + ", "
            else:
                output += str(num) + ", "
            steps += 1
            continue
        elif num % 2 != 0:
            num = num * 3 + 1
            steps += 1
            output += str(num) + ", "
            continue
    stop = time.perf_counter()
    output = output.rstrip(", ")
    output += f"\n{steps} steps\n-----------------------------------\n"
    # output += f"Calculation completed in {stop - start} seconds.\n"
    results.element.innerText = output
        

