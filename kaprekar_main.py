import sys
from pprint import pprint


display = ""

def kap(num):
    # convert to str and sort into descending order
    # num = Element("number").value
    global display
    num1_list = [n for n in num]
    num1_list.sort(reverse=True)
    # pad num1 with a zero if num1 < 1000, e.g. 1112 - 2111 = 999
    if len(num1_list) < 4:
        num1_list.append("0")
    num2_list = num1_list[::-1]
    num1 = int("".join(num1_list))
    num2 = int("".join(num2_list))
    display += f"{num1} - {num2} = {num1 - num2}\n"
    return num1 - num2

def kaprekar():
    global display
    # reset display with each new number
    display = ''
    output = Element('auto_display')
    # output.element.innerText = ""
    number = Element("number").value
    interim_result = None
    steps = [-2, -1, int(number),]
    while steps[-1] != steps[-2]:
        interim_result = kap(number)
        steps.append(interim_result)
        number = str(interim_result)
        
    output.element.innerText = display
    

def kaprekar_auto():
    num_3 = [n for n in range(100, 1000)]
    num_3_list = [str(n) for n in num_3]
    num_4 = [n for n in range(1000, 10000)]
    num_4_list = [str(n) for n in num_4]
    num_5 = [n for n in range(10000, 100000)]
    num_5_list = [str(n) for n in num_5]

    num_digits = Element("number").value
    if num_digits == "3":
        num_list = num_3_list
    elif num_digits == "4":
        num_list = num_4_list
    cumulative_steps = []
    longest_steps = []
    for number in num_list:
        orig = number
        interim_result = None
        steps = [-2, -1, int(number), ]
        while steps[-2] != steps[-1]:
            interim_result = kap(number)
            steps.append(interim_result)
            if interim_result == 0:
                break
            number = str(interim_result)
        cumulative_steps.append(steps)    

    count = 0
    cleaned_cumulative_steps = []
    for n in cumulative_steps:
        if n[-1] == 0:
            cleaned_cumulative_steps.append(n[2:])
        else:
            cleaned_cumulative_steps.append(n[2:-1])


    for n in cumulative_steps:
        if n[-1] == 0:
            count += 1
    a = ""
    for n in cleaned_cumulative_steps:
        a += f"{n}\n"
    output = Element('auto_display')
    output.element.innerText = display
