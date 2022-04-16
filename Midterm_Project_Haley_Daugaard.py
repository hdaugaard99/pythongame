# INF 360 - Programming in Python
# Haley Daugaard
# Midterm Project

# Prints text that sets up the beginning of the story and asks the user to type their name.
print ('Stranger: Hello baker!  Welcome to Sweetsville, home of sugary confections.')

bakerName = input('Stranger: What is your name? \n')

print('Stranger: It\'s nice to meet you, ' + bakerName + '. My name is Shelli Sherbet, owner of Shelli\'s Sherbet Shack.')

# Asks user for their gender, outputting a customized response depending on what is typed.
# If the user does not type either 'male' or 'female' they are asked to type either of those.
while True :
    print('Shelli: What is your gender?')
    gender = input('Please enter \'male\' or \'female\'. \n')
    if gender == 'male' :
        print('\nShelli: You are ' + gender + '. Is this correct?')
        break
    elif gender == 'female' :
        print('\nShelli: You are ' + gender + '. Is this correct?')
        break

# Asks user to confirm their gender.
genderConfirm = input('Please enter \'yes\' or \'no\'. \n')

# Allows the user the chance to input gender again and then moves them forward once they make a selection.
if genderConfirm == 'yes' :
    print('Shelli: Okay, ' + bakerName +'! I\'ll show you to your new bakery.')
elif genderConfirm == 'no' :
    while True :
        print('Shelli: What is your gender?')
        gender = input('Please enter \'male\' or \'female\'. \n')
        if gender == 'male' :
            print('\nShelli: Okay, ' + bakerName + '! I\'ll show you to your new bakery.')
            break
        elif gender == 'female' :
            print('\nShelli: Okay, ' + bakerName +'! I\'ll show you to your new bakery.')
            break

# Prints story text on the screen
print('\nNarration: You follow Shelli down Main Street, passing many different types of bakeries on the way. '
      'Your bakery is located at the center of Main Street, right next to Shelli\'s Sherbet Shack. Your plot of '
      'land includes an oven, card table, and bucket. It looks odd next to all of the extravagent buildings '
      'around it. \n')

print('Shelli: Here we are! What do you think? \n')

# Dictionary that holds the outcomes for each upcoming answer choice
firstImpression = {'polite' : 'It looks perfect!', 'rude' : 'This is it? I can\'t work here!'}

print('Narrator: As you look around, you think of what you should say. How would you like to answer?')

'''
Asks the user to pick a response type. If the user does not type one of the choices, they are asked again until
a choice is chosen. Depending on what is typed, a different response appears for each choice.
'''
impression = input('Please enter \'polite\' or \'rude\'. \n')

while True :
    
    if impression == 'polite' :
        print(firstImpression['polite'])
        print('\nShelli: I hoped you\'d think so! It doesn\'t look like much, but I just know the right baker could '
              'make this place into something truly special. \n')
        break
    elif impression == 'rude' :
        print(firstImpression['rude'])
        print('\nShelli: That\'s really what you think? I spent a lot of time looking for the beginning pieces '
              'of your bakery. \n')
        break
    else :
        impression = input('Please enter \'polite\' or \'rude\'. \n')

print('Shelli: What kind of bakery will you be opening here ' + bakerName + '?')

# Dictionary that contains outcomes of each choice for the bakeryType question
bakeryType = {'sarcastic' : 'Clearly it\'s going to be a cupcake bakery.', 'excited' : 'I have visions of owning the '
              'most popular cupcake bakery in the entire world!'}
'''
Asks user to type one of the response choices and asks again if the user types something that doesn't match.
What is typed determines the text that is outputted on the screen.
'''
bakeryTypeResponse = input('Please enter either \'excited\' or \'sarcastic\' to choose a response type. \n')
if bakeryTypeResponse == 'sarcastic' :
    print(bakeryType['sarcastic'])
elif bakeryTypeResponse == 'excited' :
    print(bakeryType['excited'])
else :
    bakeryTypeResponse = input('Please enter either \'excited\' or \'sarcastic\' to choose a response type. \n')

print('\nShelli: Are you sure a cupcake shop is the best idea considering the history of cupcakes in Sweetsville? \n')

# Dictionary that holds the answer outcomes for the cupcakeHistory choice
cupcakeHistory = {'confident' : 'History, schmistory! Whatever happened in the past doesn\'t scare me!', 'what?' :
                          'What history?'}

# Asks the user to type one of the answer choices.
cupcakeHistoryResponse = input('Please enter \'confident\' or \'what?\'. \n')

# If the user does not type one of the choices, the question is asked again. The answer determines the response output
while True :
    
    if cupcakeHistoryResponse == 'confident' :
        print(cupcakeHistory['confident'])
        print('\nShelli: But it should! Legend says that the lost cupcake cookbook, created by Queen Frosting, was destroyed '
              'decades ago in a fight for power. Cupcakes are bad news ' + bakerName + '.')
        break
    elif cupcakeHistoryResponse == 'what?' :
        print(cupcakeHistory['what?'])
        print('\nShelli: Legend says that the lost cupcake cookbook, created by Queen Frosting herself, was destroyed decades '
              'ago in a fight for power between two greedy cupcake bakers. Cupcakes kind of have a bad rep here.')
        break
    else :
        cupcakeHistoryResponse = input('Please enter \'confident\' or \'what?\'. \n')
        
print('\nShelli: The cupcake recipes from Queen Frosting\'s cookbook were the best in existence. If you had one, '
      'people might warm up to your cupcake bakery faster.')

# Dictionary that holds the answer outcomes for the getFirstRecipeLocation choice
getFirstRecipe = {'nice' : 'Do you know where I might be able to find a recipe from the Lost Cookbook of Queen Frosting?',
           'curt' : 'How am I supposed to get one? There\'s nothing in this boring town!'}

print('\nNarration: Shelli might know where to find one of the recipes from Queen Frosting\'s cookbook.')

# Asks the user to type a response that will determine the text output
getFirstRecipeLocation = input('\nPlease enter either \'nice\' or \'curt\' to determine how to ask Shelli about '
                               'the location of your first recipe.\n')
'''
If the user types something that doesn't match one of the answer choices, they are asked to input one of them.
What the user types determines the text outcome.
'''
while True :

    if getFirstRecipeLocation == 'nice' :
        print(getFirstRecipe['nice'])
        print('\nShelli: Word on the street is that Patty the Pie Baker, owner of Patty\'s Pie Shop, stumbled across one a few weeks '
              'ago. She may be willing to do you a favor if you\'re super nice to her.')
        break
    elif getFirstRecipeLocation == 'curt' :
        print(getFirstRecipe['curt'])
        print('\nShelli: Sweetsville is a refined town! And it\'s home to some of the best bakers in the world! Maybe I should '
              'just forget to mention that Patty the Pie Baker, owner of Patty\'s Pie Shop, found one and--Oops! Consider '
              'this one a freebie. If you continue to disrespect Sweetsville, you won\'t have my help!')
        break
    else :
        getFirstRecipeLocation = input('\nPlease enter either\'nice\' or \'curt\' to determine how to ask Shelli about '
                                     'the location of your first recipe.\n')

'''
This dictionary holds the location of Patty's Pie Shop. Each number corresponds to the number of spaces the user
can input in order to find Patty's Pie Shop and holds a different response.
'''
pieShopGuessNumber = {1 : 'Patty\'s Pie Shop is located more than 1 shop away, but less than 7 shops away',
                    2 : 'Patty\'s Pie Shop is 2 more spaces away from here.',
                    3 : 'Patty\'s Pie Shop is located on space 4.',
                    4 : 'You have found Patty\'s Pie Shop!',
                    5 : 'Travel one less space to find Patty\'s Pie Shop.',
                    6 : 'You have gone too far! Patty\'s Pie Shop is less than 6 spaces away, but more than 3 '
                    'spaces away.',
                    7 : 'You have gone too far! Patty\'s Pie Shop is less than 7 spaces away, but more than '
                    '3 spaces away.'}

print('\nShelli: Patty\'s Pie Shop is located a few shops down from here.')

# This code asks the user to input a number between 1 and 7. If the user guesses correct, they meet Patty.
# If the user guesses wrong, they have to guess again.
pieShopGuess = input('Please enter a number between 1 and 7 to guess how many spaces you need to move to find '
                           'Patty\'s Pie Shop. \n')
while True :
    if pieShopGuess == '1' :
        print(pieShopGuessNumber[1])
        pieShopGuess = input('Please enter a number between 1 and 7 to guess how many spaces you need to move to find '
                           'Patty\'s Pie Shop. \n')
    elif pieShopGuess == '2' :
        print(pieShopGuessNumber[2])
        pieShopGuess = input('Please enter a number between 1 and 7 to guess how many spaces you need to move to find '
                           'Patty\'s Pie Shop. \n')
    elif pieShopGuess == '3' :
        print(pieShopGuessNumber[3])
        pieShopGuess = input('Please enter a number between 1 and 7 to guess how many spaces you need to move to find '
                           'Patty\'s Pie Shop. \n')
    elif pieShopGuess == '4' :
        print(pieShopGuessNumber[4])
        break
    elif pieShopGuess == '5' :
        print(pieShopGuessNumber[5])
        pieShopGuess = input('Please enter a number between 1 and 7 to guess how many spaces you need to move to find '
                           'Patty\'s Pie Shop. \n')
    elif pieShopGuess == '6' :
        print(pieShopGuessNumber[6])
        pieShopGuess = input('Please enter a number between 1 and 7 to guess how many spaces you need to move to find '
                           'Patty\'s Pie Shop. \n')
    elif pieShopGuess == '7' :
        print(pieShopGuessNumber[7])
        pieShopGuess = input('Please enter a number between 1 and 7 to guess how many spaces you need to move to find '
                           'Patty\'s Pie Shop. \n')
    else :
        pieShopGuess = input('Please enter a number between 1 and 7 to guess how many spaces you need to move to find '
                           'Patty\'s Pie Shop. \n')

print('\nPatty: Hi! You must be ' + bakerName + '! Shelli was just here. She said you\'re looking for a recipe from '
      'Queen Frosting\'s Lost Cookbook. I have one and I\'ll give it to you, but you\'ll have gather the ingredients '
      'yourself.')

# This dictionary holds the answer outcomes for bakerThanksPatty
thankPatty = {'grateful' : 'Thank you for your Generosity, Patty!.', 'stunned' : 'I don\'t know what to say! This is '
            'amazing!'}

bakerThanksPatty = input('\nYou should thank Patty for helping you. Please enter either \'grateful\' or \'stunned\' '
                         'to thank her appropriately.\n')

# This code interprets the user's input to create an output.
while True :
    if bakerThanksPatty == 'grateful' :
        print(thankPatty['grateful'])
        print('\nPatty: Consider it a welcome present.')
        break
    elif bakerThanksPatty == 'stunned' :
        print(thankPatty['stunned'])
        print('\nPatty: It should go to a baker who will actually use it. Use it well, ' + bakerName + '.')
        break
    else :
        bakerThanksPatty = input('\nYou should thank Patty for helping you. Please enter either \'grateful\' or \'stunned\' '
                         'to thank her appropriately.')
        
print('\nNarration: After visiting Patty, you go back to your bakery and look at the recipe card. You will need to '
      'gather the ingredients, so you read the ingredient list. The ingredients are:')

# This is a set of table data for the list of ingredients
firstRecipeIngredients = [['flour', 'butter', 'salt'],
                          ['sugar', 'eggs', 'cocoa'],
                          ['powder', 'vanilla', 'water']]

# This code prints the table firstRecipeIngredients in a left justification.
def printTable(firstRecipeIngredients):
    colWidths = [0] * len(firstRecipeIngredients)

    for row in range(len(firstRecipeIngredients)):
        for column in range(len(firstRecipeIngredients[row])):
            if colWidths[row] < len(firstRecipeIngredients[row][column]):
                colWidths[row] = len(firstRecipeIngredients[row][column]) + 1

    for row in range(len(firstRecipeIngredients)):
        for column in range(len(firstRecipeIngredients)):
            print(firstRecipeIngredients[column][row].ljust(colWidths[column]), end = ' ')
        print('')

printTable(firstRecipeIngredients)
