import random
from WordList import wordList

def get_word():
    word = random.choice(word_list)
    return word.upper()
  
  def display_hangman(tries): #we could use this or just make the code display how many tries the user has left without the stickman
        stages = [ """  
                        --------
                        |    |
                        |    o
                        |   \\|/
                        |    |
                        |   / \\
                        -
                    """
                        ,
                    """
                        
                        --------
                        |     |
                        |     o
                        |    \\|/
                        |     |
                        |    /
                        -
                    """
                        ,
                    """
                        --------
                        |     |
                        |     o
                        |    \\|/
                        |     |
                        |
                        -
                    """
                        ,
                    """
                        --------
                        |     |
                        |     o
                        |    \\|
                        |     |
                        |
                        -
                    """
                        ,
                    """
                        --------
                        |     |
                        |     o
                        |     |
                        |     |
                        |
                        -
                    """
                        ,
                    """
                        --------
                        |     |
                        |     o
                        |
                        |
                        |
                        -
                    """
                        ,
                    """
                        --------
                        |     |
                        |
                        |
                        |
                        |
                        -
                    """
    ]
    return stages[tries]
