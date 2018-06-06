def divisors(n):
    divisor_list = [i for i in range(1, n + 1) if n % i == 0]
    return divisor_list


try:
    value = int(input("Prime checker: "))
except ValueError:
    print("Value must be an integer!")
else:
    if len(divisors(value)) == 2:
        print(str(value) + " is a prime.")
    else:
        print(str(value) + " is not a prime.")
