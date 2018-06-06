fibonacci = [0, 1]


def fibonacci_sequence(n):
    for i in range(n - 2):
        fibonacci.append(fibonacci[-2] + fibonacci[-1])

count = input("How many fibonacci numbers to generate? ")
if int(count) <= 2:
    print(fibonacci)
else:
    fibonacci_sequence(int(count))
    print(fibonacci)
