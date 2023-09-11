def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 2) + fib(n - 1)

if __name__ == '__main__':
    i = int(input("Enter number: "))
    print(fib(i))