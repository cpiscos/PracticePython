from random import randint

actual_number = randint(1,10)

print("I have chosen a number from 1-9")
while True:
    guess = int(input("What do you think my number is? "))
    if guess == actual_number:
        print("You are correct!")
        break
    elif guess > actual_number:
        print("Too high")
    else:
        print("Too low")