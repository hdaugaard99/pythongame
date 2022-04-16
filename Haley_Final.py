# INF 360 - Programming in Python
# Haley Daugaard
# Final Project

"""
My project is a story that makes the user a baker in Sweetsville.
The user must answer prompts to choose how to interact with characters
in the story and play a guessing game to find their way to the
first recipe they will add to their cookbook.
"""
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

import sys

logging.debug('Import helper functions')
try:
    # Import everything from helper_func
    from helper_func import *
except:
    logging.critical('OMG, something went wrong. Can\'t import helper_func.')
    print('Your helper_func.py file is missing')
    sys.exit() 

logging.debug('Main program')
def main():

    # Create Baker object
    baker = Baker()

    # Print Intro Narrative
    consolePrinter(narDict['intro'])

    # Collect Baker's name
    baker.getName()

    # Print Greeting Narrative
    consolePrinter(narDict['greeting'].format(baker.name))
    
    # Ask for Baker's Gender
    baker.getGender()

    # Print Location Narrative and Ask for First Impression
    consolePrinter(narDict['location'])
    questionPrompt(questions['firstImpression'], baker)
    questionPrompt(questions['bakeryType'], baker)

    # Ask for cupcakeHistory response
    questionPrompt(questions['cupcakeHistory'], baker)

    # Ask for getFirstRecipe response 
    questionPrompt(questions['getFirstRecipe'], baker)

    # Print pieShopLocation
    consolePrinter(narDict['pieShopLocation'])

    # Imports the number game that allows the baker to find Patty's Pie Shop
    import NumberGame

    # Print enterPieShop narrative
    consolePrinter(narDict['enterPieShop'])

    # Run receiveFirstRecipe prompt
    questionPrompt(questions['receiveFirstRecipe'], baker)

    # Print takeRecipe narrative
    consolePrinter(narDict['takeRecipe'])

    # Print table of recipe ingredients
    import FirstRecipeIngredients
                  
    # Print theFirstIngredient narrative
    consolePrinter(narDict['theFirstIngredient'])

    # Run chickenCoopIntro
    questionPrompt(questions['chickenCoopIntro'], baker)

    # Print meetEddy narration
    consolePrinter(narDict['meetEddy'])

    # Imports the riddle file and runs it
    import ChickenRiddle


logging.debug('Run main')
if __name__ == '__main__':
    main()
