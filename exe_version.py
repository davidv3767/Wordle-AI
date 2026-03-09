# Filtering helper function:
def get_possible_words(word_list, guess, feedback):
    # Parameters:
    # word_list -> list of 5-letter words
    # guess -> the word you guessed/typed
    # feedback -> the colors received (G = Green, Y = Yellow, B = Black)
    remaining_words = []
    for word in word_list:
        keep_word = True
        for i in range(5):
            letter = guess[i]
            color = feedback[i]
            if color == 'G':
                # Word should have letter in this spot
                if word[i] != letter:
                    keep_word = False
            elif color == 'Y':
                # Word should have letter, but NOT in this spot
                if letter not in word or word[i] == letter:
                    keep_word = False
            elif color == 'B':
                # Word should not have letter
                if letter in word:
                    keep_word = False
        if (keep_word):
            remaining_words.append(word)
    return remaining_words

# Loading helper function:
import os
import sys

def get_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def load_all_words(filename):
    true_path = get_resource_path(filename)
    try:
        # Open 'true_path', not 'filename'
        with open(true_path, 'r') as file:
           return [line.strip().lower() for line in file.readlines()]
    except FileNotFoundError:
        print(f"The file is not found at: {true_path}")
        return []
    
# Scorer helper function:
def rank_words(word_list):
    if not word_list:
        return[]
    else:
        # Finds letter frequency
        letter_freq = {}
        for individual_word in word_list:
            unique_letters = set(individual_word) 
            for char in unique_letters:
                letter_freq[char] = letter_freq.get(char, 0) + 1
        # Creates word scores
        word_scores = []
        for word in word_list:
            score = 0
            for letter in set(word):
                score += letter_freq.get(letter, 0)
            if len(set(word)) < len(word):
                score = score * 0.8
            word_scores.append((word, score))
        # Sort by score
        word_scores.sort(key=lambda x: x[1], reverse = True)
        # Return words in order by score
        return [pair[0] for pair in word_scores]   

# Load data from wordle_dictionary.txt
word_list = load_all_words('wordle_dictionary.txt')

# Introduce
print("Hello! I am an AI Wordle Solver!")
print(f"I have loaded {len(word_list)} words into my dictionary.") 

# Safety check
if not word_list:
    print("Stopping due to broken dictionary.")
else:
    # Simulate a Wordle game with 6 guesses
    for turn in range (1, 7):
        # Counting Turn Number
        print("Turn " + str(turn))
        # Suggesting (first one in order)
        ranked_list = rank_words(word_list)
        suggestion = ranked_list[0]
        print("Suggested Guess: " + suggestion)
        # Getting input from user
        guess = input("What word did you guess? ").lower()
        feedback = input("What were the colors given (G = Green, Y = Yellow, B = Black) ").upper()
        # Seeing if game was won
        if feedback == 'GGGGG':
            print("Yay! You found it in " + str(turn) + " turns!")
            break
        # Filter options
        word_list = get_possible_words(word_list, guess, feedback)
        if len(word_list) == 0:
            print("Wait a moment... are your colors correct?")
            break
        else:
            # Only print the list if there are 20 or fewer words
            if len(word_list) <= 15:
                clean_output = ', '.join(word_list)
                print("Words remaining: " + clean_output)
            else:
                # If the list is huge, only number is printed
                print(f"Words remaining: {len(word_list)}")