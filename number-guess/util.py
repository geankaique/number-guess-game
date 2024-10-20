def val_int(txt):
    """
    Check if number can be int
    :param txt: input message
    :return: number converted in integer
    """
    try:
        n = int(input(txt))
    except ValueError:
        print('ERROR choose a valid number!')
    else:
        return n

def difficulty_level():
    while True:
        dif = val_int('Enter your choice: ')

        if dif == 1:
            print('You have selected the Easy difficulty level.')
            print("Let's start the game!")
            return 10
        elif dif == 2:
            print('You have selected the Medium difficulty level.')
            print("Let's start the game!")
            return 5
        elif dif == 3:
            print('You have selected the Hard difficulty level.')
            print("Let's start the game!")
            return 3
        else:
            print('Invalid choice!')

def play_again():
    while True:
        again = input('Play again? [Y/N] ')
        if again[0] in 'YyNn':
            break

    if again[0] in 'Yy':
        return True
    elif again[0] in 'Nn':
        return False