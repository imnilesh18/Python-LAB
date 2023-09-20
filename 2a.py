def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


n = int(input("Enter the number: "))
if n < 0:
    print(f"The Number {n} is not a valid input.")
else:
    print("The Fibonacci Series: ")
    for i in range(0, n):
        print(fib(i), end=" ")
