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
