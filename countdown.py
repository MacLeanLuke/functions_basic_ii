# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

def countdown(number):
    for x in range(number, -1, -1):
        print(x)
    print('blastoff')

countdown(10)