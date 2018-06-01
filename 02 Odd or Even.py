value = input('Your value: ')
try:
    if int(value) % 2 == 0:
        print(value, 'is Even')
    else:
        print(value, 'is Odd')
except Exception:
    print('Value must be integer')
