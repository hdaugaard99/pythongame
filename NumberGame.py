'''
This file contains the code for a number guessing game.
'''

import random

play = True

while play == True:
    pieShopLocation = random.randint(1, 10)
    numGuess = 3
    correct = False

    print('\n It\'s time to go to Patty\'s Pie Shop. \n')
    print('You have three chances.')

    while numGuess > 0:
        print('You have ' + str(numGuess) + ' chances left. \n')
        bakerInput = input('''Pick a number between 1 and 10 to guess how many spaces
you need to move to find Patty\'s Pie Shop. \n ''')

        numGuess = numGuess - 1

        if int(bakerInput) == pieShopLocation:
            print('You have found Patty\'s Pie Shop!')
            
            correct = True
            break

        elif int(bakerInput) < 1 or int(bakerInput) > 10:
            print('Please pick a number between 1 and 10!')
            continue

        elif int(bakerInput) > pieShopLocation:
            print('You have gone too far!')
            continue

        elif int(bakerInput) < pieShopLocation:
            print('You have not gone far enough!')
            continue

    if correct == False:
        play = True

    if correct == True:
        print('It\'s time to meet Patty the Pie Baker.')
        break

        
        
