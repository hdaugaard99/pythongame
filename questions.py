"""
This file stores all the question dictionaries.

Question List Fields

========
Required
========

Field            Type      Explanation
===============================================
question_name    str       Name of the Question
question         str       The question you wish to ask
prompt           str       Prompt text. Surround in ''' and end with \n
answers          dict      A dictionary of possible answers and responses.
                           Responses should be a in a list, even if it is just one.
need_confirm     bool      True or False

================================
Required if need_confirm is True
================================

Field            Type      Explanation
===============================================

confirmation     str       Confirmation text
confirm_prompt   str       Confirmation prompt text. Surround in ''' and end with \n
pos_confirm      str       Yes response text

"""

# Add to the questionList below:
questionList = [
    {
        'question_name': 'gender',
        'question': 'Shelli: What is your gender?',
        'prompt': '''Please enter 'male' or 'female'.\n''',
        'answers': {
            'male': None,
            'female': None
            },
        'need_confirm': True,
        'confirmation': 'Shelli: You are {}. Is this correct?\n',
        'confirm_prompt': '''Please enter 'yes' or 'no'.\n''',
        'pos_confirm': 'Shelli: Okay, {}! I\'ll show you to your new bakery.'  
        },
    {
        'question_name': 'firstImpression',
        'question': 'Shelli: Here we are! What do you think? \n',
        'prompt': '''Please enter 'polite' or 'rude'.\n''',
        'answers': {
            'polite': ['''
                        {}: It looks perfect!
                        ''',
                        '''
                        Shelli: I hoped you'd think so! It doesn't look like
                        much, but I just know the right baker could make this
                        place into something truly special.
                        ''',
                        ],
            'rude':   ['''
                        {}: This is it? I can't work here!
                        ''',
                        '''
                        Shelli: That's really what you think? I spent a lot
                        of time looking for the beginning pieces of your
                        bakery.
                        ''',
                        ]
                    },
        'need_confirm': False,
        },
    {
        'question_name': 'bakeryType',
        'question': '''Shelli: What kind of bakery will you be opening here? \n''',
        'prompt': '''Please enter either 'excited' or 'sarcastic'.\n''',
        'answers': {
            'sarcastic': ['''
                            {}: Clearly it's going to be a cupcake bakery.
                            ''',
                           
                            ],
            'excited': ['''
                        {}: I have visions of owning the most popular cupcake bakery
                        in the entire world!
                        ''',
                        
                        ]
                    },
            'need_confirm': False,
            },
    {
        'question_name': 'cupcakeHistory',
        'question': '''Shelli: Are you sure a cupcake shop is the best idea considering
the history of cupcakes in Sweetsville? \n''',
        'prompt': '''Please enter either 'confident' or 'what?'. \n''',
        'answers': {
            'confident': ['''
                            {}: History, schmistory! Whatever happened in the past
                            doesn't scare me! \n
                            ''',
                          '''
                          Shelli: But it should! Legend says that the lost cupcake
                          cookbook, created by Queen Frosting, was destroyed decades
                          ago in a fight for power. Cupcakes are bad news {}.
                        
                            ''',
                           
                            ],
            'what?': ['''
                        {}: What history?
                        ''',
                      '''
                        Shelli: Legend says that the lost cupcake cookbook, created
                        by Queen Frosting herself, was destroyed decades ago in a fight
                        for power between two greedy cupcake bakers. Cupcakes kind of
                        have a bad rep here. \n
                        ''',
                        ]
                    },
            'need_confirm': False,
            },
    {
        'question_name': 'getFirstRecipe',
        'question': '''Shelli: The cupcake recipes from Queen Frosting's cookbook were
the best in existence. If you had one, people might warm
up to your cupcake bakery faster \n''',
        'prompt': '''Please enter either 'nice' or 'curt' to determine how to ask Shelli
about the location of your first recipe. \n''',
        'answers': {
            'nice': ['''
                        {}: Do you know where I might be able to find a recipe from the
                        Lost Cookbook of Queen Frosting? \n
                        ''',
                     '''
                        Shelli: Word on the street is that Patty the Pie Baker, owner of
                        Patty's Pie Shop, stumbled across one a few weeks ago. She may be
                        willing to do you a favor if you're super nice to her. \n
                        ''',
                     ],
            'curt': ['''
                        {}: How am I supposed to get one? There's nothing in this boring
                        town! \n
                        ''',
                     '''
                        Shelli: Sweetsville is a refined town! And it's home to some of
                        the best bakers in the world! Maybe I should just forget to
                        mention that Patty the Pie Baker, owner of Patty's Pie Shop,
                        found one and--Ooops!
                        Consider this one a freebie. If you continue to disrespect
                        Sweetsville, you won't have my help! \n
                        ''',
                         ]
                },            
            'need_confirm': False,
            },
    {
        'question_name': 'receiveFirstRecipe',
        'question': '''Patty: Hi! You must be the new baker in town! Shelli was just
here. She said you're looking for a recipe from Queen
Frosting\'s Lost Cookbook. I have one and I\'ll give
it to you, but you\'ll have to gather the ingredients
yourself. \n''',
        'prompt': '''You should thank Patty for helping you. Please enter either
'grateful' or 'stunned' to thank her properly. \n''',
        'answers': {
            'grateful': ['''
                        {}: Thank you for your generosity, Patty! \n
                        ''',
                     ],
            'stunned': ['''
                        {}: I don't know what to say! This is amazing! \n
                        ''',
                         ]
                },            
            'need_confirm': False,
            },
    {
        'question_name': 'chickenCoopIntro',
        'question': '''Chicken: Hold it right there, buddy. Who do you
think you are, trying to waltz into the
Chicken Coop unannounced? \n''',
        'prompt': '''Answer carefully. This chicken seems to
be ready for a fight!
Please enter 'introduction' or 'ignore' to choose a response. \n''',
        'answers': {
            'introduction': ['''
                            {}: My name's -- \n 
                        '''
                             '''
                            Chicken: I don't care what your name is. I know
                            you're trying to become a baker in Sweetsville.
                            What you need to know is, nobody comes to the
                            Chicken Coop without announcing their bakery
                            to all of Sweetsville. \n
                            ''',
                     ],
            'ignore': ['''
                        Chicken: Where do you think you're going? You can't
                        just come waltzing up to the Chicken Coop and expect
                        us to cater to your needs. You have to earn our help. \n
                        ''',
                         ]
                },            
            'need_confirm': False,
            },    

                         
    
        
    
    
                
    # Add next entry here
]
