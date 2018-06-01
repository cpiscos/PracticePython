value = int(input('What value would you like to know the divisors of: '))
divisors = [i for i in range(1, value+1) if value % i == 0]
print(divisors)