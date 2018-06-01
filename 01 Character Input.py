from datetime import datetime as dt
name = input('Enter your name: ')
hundred_delta = 100 - int(input('Enter your age: '))
print(name, 'will be 100 years old on year: ', dt.today().year+hundred_delta)