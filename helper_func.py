"""
This file contains helper functions
"""

# Built-In modules needed
import textwrap
import sys

# Import questions.py
try:
    from questions import questionList
except:
    logging.critical('OMG, something\'s wrong! Check your questionList file.')
    print('Your questions.py file is missing')
    sys.exit()

# Import narrative.py
try:
    # This will import the narDict dictionary
    from narrative import narDict
except:
    logging.critical('OMG! Can\'t import narDict. Everything is exploding.')
    print('Your narrative.py file is missing')
    sys.exit()

# Baker Object
class Baker():
    name = ''
    gender = ''

    def getName(self):
        self.name = input('Stranger: What is your name? \n')
        return self.name

    def getGender(self):
        self.gender = questionPrompt(questions['gender'], self)

# Question Object
class Question():
    # Required default values
    question_name = ''
    question = ''
    prompt = ''
    answers = ''
    need_confirm = False


    # Takes a question dictionary and coverts to objects
    def importQuestion(self, item):
        # Create required values
        self.question_name = item['question_name']
        self.question = item['question']
        self.prompt = item['prompt']
        self.answers = item['answers']
        self.need_confirm = item['need_confirm']

        # Check if additional fields are needed
        if item['need_confirm'] == True:
            # Add fields
            self.confirmation = item['confirmation']
            self.confirm_prompt = item['confirm_prompt']
            self.pos_confirm = item['pos_confirm']

# Function to wrap long paragraph to 70 characters so words don't get cut off
def consolePrinter(string, newline=True):
    # If newline is set to True, start by printing empty line.
    if newline == True:
        print('\n')

    # Wrap line to 70 characters and remove any indentions
    for line in textwrap.wrap(textwrap.dedent(string)):
        print(line)

# Function to create a list of question objects
def buildQuestions(questionList):
    questionObjs = {}
    for item in questionList:
        try:
            # Create Object
            obj = Question()
            obj.importQuestion(item)

            # Add object to list
            questionObjs[obj.question_name] = obj
        except:
            print('Failed to build object')
    return questionObjs

questions = buildQuestions(questionList)

def questionPrompt(obj, baker):
    # This function will prompt the user for a question from a dictionary.
    # If there is an answer for this question, it will check it.
    # If there is no check needed, it will return the input.
    # Start answer loop
    consolePrinter(obj.question)
    while True:
        # Print the question
        answer = input(obj.prompt)

        # Check if answer in answers dict and needs confirmation
        if answer in obj.answers.keys() and obj.need_confirm == True:
            consolePrinter(obj.confirmation.format(answer))
            while True:
                confirmation = input(obj.confirm_prompt)
                if confirmation == 'yes':
                    consolePrinter(obj.pos_confirm.format(baker.name))
                    break
                elif confirmation == 'no':
                    break
            # Needed to exit outside prompt only if a yes confirmation
            if confirmation == 'yes':
                break

        # Check if answer in answers dict and return message if available if no confirmation needed
        elif answer in obj.answers.keys() and obj.need_confirm == False:
            # Print multiple lines
            for line in obj.answers[answer]:
                consolePrinter(line.format(baker.name))
            break
