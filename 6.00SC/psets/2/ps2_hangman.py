# ----------------------------------------------------------------------------------------------------------------------
#
#   6.00 Problem Set 3 - Hangman
#
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# - Helper Code -
# (You don't need to understand this helper code.)
import random
import string

WORDLIST_FILENAME = "words.txt"

# This function loads a dictionary of words from a file.
def load_words():
    """
        Returns a list of valid words. Words are strings of lowercase letters.
        
        Depending on the size of the word list, this function may
        take a while to finish.
        """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

# This function chooses a random word from the loaded dictionary.
def choose_word(wordlist):
    """
        wordlist (list): list of words (strings)
        
        Returns a word from wordlist at random
        """
    return random.choice(wordlist)

# - End of Helper Code -
# ----------------------------------------------------------------------------------------------------------------------


# --- Libraries ---
import string


# --- Constants ---
# This value was obtained by multiplying the length of the longest word in the dictionary by 1.5. The following code
# snippet was used to obtain the aforementioned length:
#
#   wordlist.sort(key=len, reverse=True)
#   print len(wordlist[0])
#
MAX_GUESSES = 15


# --- Functions ---
def hangman(dict):
    """
    Start up and carry out an interactive Hangman game between a player
    and the computer.
    """
    # Set up the game of Hangman.
    word = choose_word(dict)
    letters = list(string.ascii_lowercase)
    answer = ['_'] * len(word)
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is", len(word), "letters long."
    print "=" * 13
    
    # Carry out the game of Hangman.
    won = False
    guesses = MAX_GUESSES
    while guesses > 0:
        # Show player the status of the game
        print "You have", guesses, "guesses left."
        print "Avalailable letters", ''.join(letters)
        # Prompt player for input
        guess = raw_input("Please guess a letter: ")
        # Evaluate player input
        # - Correct Guess
        if guess in word:
            # -- Update player answer string
            for i in range(len(word)):
                if word[i] == guess:
                    answer[i] = guess
            # -- Update list of possible guesses
            letters.remove(guess)
            print "Good guess:", ''.join(answer)
        # - Incorrect Guess
        else:
            # -- Update list of possible guesses
            letters.remove(guess)
            print "Oops! That letter is not in my word:", ''.join(answer)
        print "=" * 13
        # Evaluate win condition
        if not '_' in answer:
            won = True
            break
        # Update loop variables
        guesses = guesses - 1
    
    if won:
        print "Congratulations, you won!"
    else:
        print "Too bad. The word was", word + "."

# ----------------------------------------------------------------------------------------------------------------------
# Load the dictionary of words and point to it with the 'wordlist' variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# Your code begins here!
# ----------------------------------------------------------------------------------------------------------------------

hangman(wordlist)
