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
                # Word does have letter in this spot
                if word[i] != letter:
                    keep_word = False
            elif color == 'Y':
                # Word does have letter, but NOT in this spot
                if letter not in word or word[i] == letter:
                    keep_word = False
            elif color == 'B':
                # Word doesn't have letter
                if letter in word:
                        keep_word = False
        if keep_word:
            remaining_words.append(word)
    return remaining_words

# Looping the "brain" like in an actual Wordle game:

# Initial list of words
word_list = ['cooks', 'clubs', 'hacks', 'never', 'slate', 'trace', 'shack', 'slack', 'hated']

# Introduction of program
print("I am a Wordle AI Solver!")
print(f"I have {len(word_list)} words in my dictionary.")

# Loop to simulate a Wordle game with 6 turns
for turn in range(1, 7):
    # Counting Turn #
    print("Turn " + str(turn))
    suggestion = word_list[0]
    # Suggesting (first one in order)
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
        clean_output = ', '.join(word_list)
        print("Words remaining: " + clean_output)
