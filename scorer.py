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
