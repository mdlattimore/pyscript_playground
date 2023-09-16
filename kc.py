print("Enter a 4 digit number. The only rule is that at least one digit must be different than the others")
number = input("> ")



K_CONST = 6174

def kap(num):
    # convert to str and sort into descending order
    num1_list = [n for n in num]
    num1_list.sort(reverse=True)
    num2_list = num1_list[::-1]
    num1 = int("".join(num1_list))
    num2 = int("".join(num2_list))
    return num1 - num2

interim_result = None
steps = [-2, -1]
while steps[-1] != steps[-2]:
    interim_result = kap(number)
    steps.append(interim_result)
    number = str(interim_result)

print(steps[2:])