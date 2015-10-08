# ---------------------------------------------------------------------------------------------------------------------
#
# 6.00 Problem Set 3A Solutions
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
#
# ---------------------------------------------------------------------------------------------------------------------


import random
import string


# --- Constants ---
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

WORDLIST_FILENAME = "words.txt"

SCRABBLE_LETTER_VALUES = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}


# Helper Code (you don't need to understand this helper code)
# ---------------------------------------------------------------------------------------------------------------------
#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
        Returns a random hand containing n lowercase letters.
        At least n/3 the letters in the hand should be VOWELS.
        
        Hands are represented as dictionaries. The keys are
        letters and the values are the number of times the
        particular letter is repeated in that hand.
        
        n: int >= 0
        returns: dictionary (string -> int)
        """
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
        Displays the letters currently in the hand.
        
        For example:
        display_hand({'a':1, 'x':2, 'l':3, 'e':1})
        Should print out something like:
        a x x l l l e
        The order of the letters is unimportant.
        
        hand: dictionary (string -> int)
        """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              # print all on the same line
    print                               # print an empty line

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------
#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
        Returns the score for a word. Assumes the word is a
        valid word.
        
        The score for a word is the sum of the points for letters
        in the word multiplied by the length of the word, plus 50
        points if all n letters are used on the first go.
        
        Letters are scored as in Scrabble; A is worth 1, B is
        worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.
        
        word: string (lowercase letters)
        returns: int >= 0
        """
    score = 0
    for char in word:
        score = score + SCRABBLE_LETTER_VALUES[char]
    score = score * len(word)
    
    # award bonus points for using all letters
    if len(word) == n:
        score = score + 50
    
    return score
# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------
#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
	In other words, this assumes that however many times
	a letter appears in 'word', 'hand' has at least as
	many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    hand_dict = hand.copy()
    word_dict = get_frequency_dict(word)
    for i in word_dict.keys():
        letter_count = word_dict[i]
        # remove key-value pair if all letters used; decrement otherwise
        if hand[i] - letter_count == 0:
            del hand_dict[i]
        else:
            hand_dict[i] = hand_dict[i] - letter_count
    return hand_dict
# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------
#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    # check if word is in word list
    in_word_list = word in word_list
    if not in_word_list:
        return False
    
    # check if word used letters in hand
    word_dict = get_frequency_dict(word)
    letters_in_hand = True
    for i in word_dict.keys():
        if not (i in hand and word_dict[i] <= hand[i]):
            letters_in_hand = False
    
    return letters_in_hand
            

def calculate_handlen(hand):
    handlen = 0
    for v in hand.values():
        handlen += v
    return handlen
# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------
#
# Problem #4: Playing a hand
#
def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      
    """
    sum = 0
    input = ""
    while len(hand) > 0:
        # print current hand
        print "Current Hand:\t",
        display_hand(hand)
        
        # get user input
        input = raw_input("Enter word, or a \".\" to indicate that you are finished: ")
        if input == ".":
            break
        
        # evaluate input
        if is_valid_word(input, hand, word_list):
            hand = update_hand(hand, input)
            score = get_word_score(input, HAND_SIZE)
            sum = sum + score
            print "\"" + input + "\" earned", score, "points. Total:", sum, "points." 
        else:
            print "Invalid word, please try again."
        
        # print a new line
        print

    #print final score
    print "Total score:", sum, "points."
# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------
#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    input = ""
    hand = None
    while True:
        # print menu
        print "\nMENU"
        print "\'n\' - play game with new (random) hand"
        print "\'r\' - repeat previous game"
        print "\'e\' - exit game\n"
        
        # get user input
        input = raw_input("Enter your choice: ")
        print
        
        # evaluate input
        if input == "n":
            hand = deal_hand(HAND_SIZE)
            play_hand(hand, word_list)
        elif input == "r":
            if hand != None:
                play_hand(hand, word_list)
            else:
                print "ERROR: no previous game in this session"
        elif input == "e":
            return
        else:
                print "ERROR: invalid input"
# ---------------------------------------------------------------------------------------------------------------------


# Main
# ---------------------------------------------------------------------------------------------------------------------
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
