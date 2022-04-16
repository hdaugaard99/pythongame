'''
This program defines the firstRecipeIngredients table
and defines the printTable function.
'''

# Defines firstRecipeIngredients table
firstRecipeIngredients = [['flour', 'butter', 'salt'],
                            ['sugar', 'eggs', 'cocoa'],
                            ['powder', 'vanilla', 'water']]

# Defines printTable function
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

# Prints firstRecipeIngredients table
printTable(firstRecipeIngredients)
