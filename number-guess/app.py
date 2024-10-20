from random import randint
from util import val_int, difficulty_level, play_again
plays = win =  0

print('Welcome to the Number Guessing Game!')

while True:
    print("I'm thinking of a number between 1 and 100.")
    print('Select the difficulty level: ')
    print('[ 1 ] Easy (10 chances)')
    print('[ 2 ] Medium (5 chances)')
    print('[ 3 ] Hard (3 chances)')
    chances = difficulty_level()

    number = randint(1,100)
    cont = 0
    while chances != 0:
        chances -= 1
        cont += 1

        userInput = int(input('Choose a Number between 1 and 100: '))
        if userInput == number:
            print(f'Congratulations you beat the game with {cont} attempts')
            win += 1
            break
        elif chances == 0: # Check if is the last lace
            print(f'GAME OVER the number was {number}')
            break
        elif userInput > number:
            print(f'Incorrect! The number is less than {userInput}.')
        elif userInput < number:
            print(f'Incorrect! The number is greater than {userInput}.')

    plays += 1
    if not play_again():
        break



print(f'You played {plays} times and won {win} times')