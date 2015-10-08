from ps3a import *
import time
from perm import *


# ---------------------------------------------------------------------------------------------------------------------
#
#
# Problem #6A: Computer chooses a word
#
#
def choose_best_word(hand, word_list):
    # get all permutations of hand
    perms = []
    for i in range(len(hand), 0, -1):
        perms.extend(get_perms(hand, i))
    
    # prune list of permutations
    best = (None, -1)
    for perm in perms:
        if perm in word_list:
            score = get_word_score(perm, HAND_SIZE)
            if score > best[1]:
                best = (perm, score)
    
    return best[0]


def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    return choose_best_word(hand, word_list)
# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------
#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TODO - change this to proper method
    sum = 0
    while len(hand) > 0:
        # print current hand
        print "Current Hand:\t",
        display_hand(hand)
        
        # get computer's choice
        word = comp_choose_word(hand, word_list)
        if word == None:
            break
        
        # evaluate word
        hand = update_hand(hand, word)
        score = get_word_score(word, HAND_SIZE)
        sum = sum + score
        print "\"" + word + "\" earned", score, "points. Total:", sum, "points."
        
        # print a new line
        print
    
    #print final score
    print "Total score:", sum, "points."  
# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------
#
# Problem #6C: Playing a game
#
#
def print_menu():
    print "\nMENU"
    print "\'n\' - play game with new (random) hand"
    print "\'r\' - repeat previous game"
    print "\'e\' - exit game\n"

def print_submenu():
    print "SUB-MENU"
    print "\'u\' - team human: play the game yourself"
    print "\'c\' - team computer: watch the computer play\n"

def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    input = ""
    hand = None
    while True:
        print_menu()
        
        # get user input
        input = raw_input("Enter your choice: ")
        print
        
        # evaluate input
        if input == "e":
            return
            
        if input == "n" or input == "r":
            # set hand
            if input == "n":
                hand = deal_hand(HAND_SIZE)
            if input == "r" and hand == None:
                print "ERROR: no previous game in this session"
                continue
            
            print_submenu()
            
            # get user input
            input = raw_input("Enter your choice: ")
            print
            
            if input == "u":
                play_hand(hand, word_list)
            elif input == "c":
                comp_play_hand(hand, word_list)
            else:
                print "ERROR: invalid input"
        else:
            print "ERROR: invalid input"
# ---------------------------------------------------------------------------------------------------------------------
        
#   Main
# ---------------------------------------------------------------------------------------------------------------------
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
