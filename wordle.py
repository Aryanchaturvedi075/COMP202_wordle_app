# Author: Aryan Chaturvedi 260976059
# Assignment 2 Question 2

# calling the necessary modules
import random
# importing the functions from the wordle_util module
from wordle_utils import *

# Defining the global variables
WORDLE_WORD_LENGTH = 5
MAX_NUM_OF_GUESSES = 6
CHAR_GREEN = '\x1b[6;30;42m'
CHAR_YELLOW = '\x1b[6;30;43m'
CHAR_GRAY = '\x1b[6;30;47m'
CHAR_END = '\x1b[0m'

# Helper Functions
# Function 1
def is_valid_word(word, word_list):
    """(str, list) -> bool
    Returns a boolean output of whether a word is valid or not
    >>> is_valid_word('about', ['abounds', 'about', 'abouts', 'above', 'aboveboard'])
    True
    >>> is_valid_word('about', ['abounds', 'abouts', 'above', 'aboveboard'])
    False
    >>> is_valid_word('aloha', ['above', 'about', 'aloha', 'adore'])
    True
    """
    # condition checking if the word 1 5 letters and in the provided list
    if len(word) == WORDLE_WORD_LENGTH and word in word_list:
        return True
    else:
        return False
  

# Function 2
def print_string_list(word_list):
    """(list) -> NoneType
    Void function that simply prints the elements of a list on a new line
    >>> print_string_list(['abounds', 'about'])
    abounds
    about
    >>> print_string_list(['hello', 'goodbye'])
    hello
    goodbye
    >>> print_string_list(['daytime', 'nighttime'])
    daytime
    nighttime
    """
    # for loop printing out each element of the list on a new line
    for i in word_list:
        print(i)
   

# Function 3
def color_string(word, color):
    """(str, int) -> str
    Returns a colored string word
    
    >>> color_string('about', 'green')
    '\x1b[6;30;42mabout\x1b[0m'
    
    >>> color_string('hello', 'yellow')
    '\x1b[6;30;43mhello\x1b[0m'
    
    >>> color_string('melon', 'brown')
    Invalid color
    'melon'
    """
    # list of the valid colours
    color_list = ['green', 'yellow', 'gray']
    # list of ANSI_colour eliminates the need for if_else conditions
    ANSI_list = [CHAR_GREEN, CHAR_YELLOW, CHAR_GRAY]
    # this variable will be returned at the end of the function
    colour_string = word
    
    # compares if the color is part of the specified list
    if color not in color_list:
        print('Invalid color')
    else:
        # assigns corresponding ANSI code of colour
        index = color_list.index(color)
        # sandwich the word in between
        colour_string = ANSI_list[index] + colour_string + CHAR_END
    
    # only gives the string output, does not actually print the coloured string
    return colour_string


# Function 4
def get_all_5_letter_words(string_list):
    """(list) -> list
    Returns a list of all the 5 letter words in the input list
    
    >>> get_all_5_letter_words(['abs', 'about', 'abouts', 'above', 'aboveboard', 'aloft'])
    ['about', 'above', 'aloft']
    >>>get_all_5_letter_words(['under', 'neath', 'underneath', 'the', 'dining', 'table'])
    ['under', 'neath', 'table']
    >>> get_all_5_letter_words(['hello', 'there', 'general', 'kenobi'])
    ['hello', 'there']
    """
    word_list = [] # create empty list
    # iterates through each element in the list
    for i in string_list:
        # condition to check if element is a 5 letter word
        if len(i) == WORDLE_WORD_LENGTH:
            # append element to new_list
            word_list.append(i)
    return word_list


# Additional Helper function used in Functions 9 and 10
def get_correct_input(user_input, list_of_options, prompt_message, invalid_input_prompt):
    """(str, list, str, str) -> str
    Returns a user's choice after validating the input
    >>> get_correct_input(user_input, list_of_options, 'Type a word: ', 'Word not in list.')
    Type a word: hello
    'hello'
    
    >>> get_correct_input(user_choice, int_list, 'Pick a number ', 'Number not in list.')
    Pick a number 3
    Number not in list.
    Pick a number 1
    '1'
    """
    # while loop starts to allow user input, calls on the is_valid_word() function
    while is_valid_word(user_input, list_of_options) == False:
        # prompt message is displayed
        user_input = input(prompt_message)
        # assumption that all alphabetic characters will be lowercase
        user_input = user_input.lower()
        # condition to end the loop before printing invalid input statement
        if user_input in list_of_options:
            break
        print(invalid_input_prompt)
    return user_input


# Main Functions
# Function 5
def compare_and_color_word(guessed_word, correct_word):
    """(str, str) -> str
    Returns a coloured format of the guessed_word string, possibly indicating part of the
    correct_word
    >>> compare_and_color_word('mount', 'about')
    '\x1b[6;30;47mm\x1b[0m\x1b[6;30;43mo\x1b[0m\x1b[6;30;43mu\x1b[0m\x1b[6;30;47mn
    \x1b[0m\x1b[6;30;43mt\x1b[0m'
    
    >>> compare_and_color_word('above', 'below')
    '\x1b[6;30;47ma\x1b[0m\x1b[6;30;43mb\x1b[0m\x1b[6;30;43mo\x1b[0m\x1b[6;30;47mv
    \x1b[0m\x1b[6;30;43me\x1b[0m'
    
    >>> compare_and_color_word('hello', 'howdy')
    '\x1b[6;30;42mh\x1b[0m\x1b[6;30;47me\x1b[0m\x1b[6;30;47ml\x1b[0m\x1b[6;30;47ml
    \x1b[0m\x1b[6;30;43mo\x1b[0m'
    """
    evaluated_string = ''
    # for loop comparing both words by their index
    for i in range(WORDLE_WORD_LENGTH):
        
        # if character is in the right position, colour is green
        if guessed_word[i] == correct_word[i]:
            evaluated_string += color_string(guessed_word[i], 'green')
            
        # otherwise if letter is part of the wordle, colour it yellow
        elif guessed_word[i] in correct_word:
            evaluated_string += color_string(guessed_word[i], 'yellow')
            
        # else colour it gray
        else:
            evaluated_string += color_string(guessed_word[i], 'gray')
            
    return evaluated_string


# Function 6
def print_final_message(num_of_guesses, correct_word):
    """(int, str) -> NoneType
    Void function that displays whether the user won or lost
    >>> print_final_message(6, 'about')
    You won! It took you 6 guesses.
    >>> print_final_message(1, 'above')
    You won! It took you 1 guess.
    >>> print_final_message(7, 'birch')
    You lost! The word was birch
    """
    # condition to check if the user won or lost
    if num_of_guesses <= MAX_NUM_OF_GUESSES:
        print("You won! It took you", num_of_guesses, end =' ')
        
        # second condition to check if the user guessed in 1 try
        if num_of_guesses == 1:
            print("guess.")
        else:
            print("guesses.")
            
    else: # print statement and the correct word
        print("You lost! The word was", color_string(correct_word, 'green'))


# Function 7
def input_wordle(word_list):
    """(list) -> str
    Returns user's choice of wordle
    """
    # empty string so that the while loop can start
    user_input = ''
    # while loop ensures that the word is within the provided word_list
    while is_valid_word(user_input, word_list) == False:
        
        # input_and_hide() function hides user response after 2 seconds
        user_input = input_and_hide("Input today's word: ")
        # imported from wordle_utils module
        
        user_input = user_input.lower() # convert all letters to lowercase
        
        # condition breaks loop if input is valid
        if user_input in word_list:
            break
        print("Not a valid word, please enter a new one.")
    
    return user_input


# Function 8
def generate_random_wordle(word_list):
    """(list) -> str
    Returns a randomly selected word from the list
    
    >>> random.seed(100)
    >>> generate_random_wordle(['about', 'above', 'aloft', 'aeons'])
    'above'
    
    >>> random.seed(69)
    >>> generate_random_wordle(['where', 'there', 'stare', 'blare'])
    'where'
    
    >>> random.seed(4200)
    >>> generate_random_wordle(['house', 'mouse', 'couch', 'louse'])
    'mouse'
    """
    # since index is one lower, want to be inclusive of the len(word_list) -1 
    index = random.randint(0, len(word_list) - 1)
    # picks corresponding element from the list
    correct_word = word_list[index]
    
    return correct_word


#Function 9
def play_with_word(correct_word, word_list):
    """(str, list) -> int
    Returns no of guesses after prompting the user to guess the word
    
    >>> play_with_word('canon', ['canon', 'armor', 'chain', 'train'])
    Enter a guess: canon
    canon
    1
    >>> play_with_word('caper', ['cable', 'cater', 'crane', 'carve', 'caper', 'calls'])
    Enter a guess: carve
    carve
    Enter a guess: crane
    carve
    crane
    Enter a guess: cable
    carve
    crane
    cable
    Enter a guess: calls
    carve
    crane
    cable
    calls
    Enter a guess: cater
    carve
    crane
    cable
    calls
    cater
    Enter a guess: crane
    carve
    crane
    cable
    calls
    cater
    crane
    7
    """
    guessed_list = [] # list will store all the user's guesses
    for num_of_guesses in range(1, MAX_NUM_OF_GUESSES+1): # loop runs from index 1 to 6
        
        # calling the get_correct_input to get valid user input
        guessed_word = ''
        guessed_word = get_correct_input(guessed_word, word_list, 'Enter a guess: ',
                                         'Not a valid word, please enter a new one.')
        # compare the guessed_word to the wordle
        comparison = compare_and_color_word(guessed_word, correct_word)
        guessed_list.append(comparison)  # append comparison to the list
        
        print_string_list(guessed_list) # prints list of all guessed words so far
        
        # if user guesses the wordle before the end of the for loop
        if guessed_word == correct_word:
            return num_of_guesses # number of guesses is returned
    
    # if for loop did not end previously then the user has not guessed the correct word
    return MAX_NUM_OF_GUESSES + 1


# Function 10
def choose_mode_and_wordle(word_list):
    """(list) -> str
    Returns the wordle i.e. the correct_word, after asking the user's prefer game mode
    >>> random.seed(20)
    >>> choose_mode_and_wordle(['about', 'above', 'aloft', 'aeons']) 
    Enter the number of players: 1
        'above'
    
    >>> choose_mode_and_wordle(['below', 'bound', 'birth', 'brain'])
    Enter the number of players: 2
    
    ***** Player 1's turn. *****
    
    ***** Player 2's turn. ***** 
    'brain'
    
    >>> choose_mode_and_wordle(['chump', 'clump', 'trump', 'slump'])
    Enter the number of players: 3
    Wordle can be played with 1 or 2 players. Please only enter 1 or 2.
    Enter the number of players: 2

    ***** Player 1's turn. *****                                                                 
    Not a valid word, please enter a new one.                                                                
    Not a valid word, please enter a new one.
    
    ***** Player 2's turn. ***** 
    'slump'
    """
    # calling the get_correct_input to get valid user input
    game_mode = ''
    int_list = ['1', '2'] # options to pick from
    game_mode = get_correct_input(game_mode, int_list, 'Enter the number of players: ',
                'Wordle can be played with 1 or 2 players. Please only enter 1 or 2.')
    # single_player mode calls generate_random_wordle() function
    if game_mode == '1':
        correct_word = generate_random_wordle(word_list)
    
    # double-player mode calls input_wordle() function to collect player 1's wordle
    else:
        print("\n***** Player 1's turn. ***** \n")
        correct_word = input_wordle(word_list)
        print("\n***** Player 2's turn. ***** \n")
    
    return correct_word


# Function 11
def play(word_list):
    """(list) -> NoneType
    Void Function which runs the game for the user and prints the result
    """
    # calling the choose_mode_and_wordle() function to get the wordle of the day
    correct_word = choose_mode_and_wordle(word_list)
    
    # calling the play_with_word() function to get number of guesses the user took
    num_of_guesses = play_with_word(correct_word, word_list)
    
    # outputing the final result of the game
    print_final_message(num_of_guesses, correct_word)
    

# Function 12
def main():
    """() -> NoneType
    """
    # calls the load_words() function from the wordle_utils module
    dictionary_list = load_words()
    
    # filter only the 5 lettered words from the list
    word_list = get_all_5_letter_words(dictionary_list)
    
    # execute the play() function and runs the wordle game
    play(word_list)