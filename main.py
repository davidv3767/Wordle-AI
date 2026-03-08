# Import functions in
from loader import load_all_words
from filtering import get_possible_words
from scorer import rank_words

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