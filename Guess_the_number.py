# Guess the number
import random

lowDigit = 10
highDigit = 50
digit = 0

countInput = 0
win = False
playGame = True
x = 0
startScore = 100
score = 0
maxScore = 0

# __________________________________________
while playGame:
    digit += random.randint(lowDigit, highDigit)
    print('The computer guessed a number, try to guess!')

    # __________________________
    while not win:
        x = ''
        while not x.isdigit():
            x = input(f'Enter a number from {lowDigit} to {highDigit}: ')
            if not x.isdigit():
                print('Please enter a number')

        x = int(x)
        if x > digit:
            print('The hidden number is less')
        if x < digit:
            print('The hidden number is greater')

        if x == digit:
            print('You won')
            win = True
            digit = 0

    if input('Enter - Gema, 0 - Finish: ') == '0':
        playGame = False
    else:
        win = False
