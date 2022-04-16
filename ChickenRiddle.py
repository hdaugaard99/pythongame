'''
This file contains the code for the chicken riddle.
'''
# Asks for user input for riddle
riddle = input('The riddle is: Why did the chicken cross the road? \n')

# Determines if user input matches and picks a response
while True:
    
    if riddle == 'to get to the other side' :
        print('You are very wise. I could not stump you. \n'
              'As promised, here are enough eggs for your first recipe. \n')

        break

    else :
        print('You did not answer correctly. Try again. \n')
        riddle = input('The riddle is: Why did the chicken cross the road? \n')
