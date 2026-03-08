# Simulates an amount of Wordle games to help testing

import random
from loader import load_all_words
from filtering import get_possible_words
from scorer import rank_words

def get_auto_feedback(guess, secret):
    # Automatically makes GYB string
    feedback = ""
    for i in range(5):
        if guess[i] == secret[i]:
            feedback += "G"
        elif guess[i] in secret:
            feedback += "Y"
        else:
            feedback += "B"
    return feedback

def run_simulation(iterations=100):
    # Setting up simulation
    all_words = load_all_words('wordle_dictionary.txt')
    stats = []
    print("Starting simulation of Wordle games (unlimited # of turns) now...")
    for i in range(iterations):
        # Set up game/round
        secret_word = random.choice(all_words)
        current_list = list(all_words)
        turns = 0
        # Do a turn
        while True:
            # Guess word
            turns += 1
            suggestion = rank_words(current_list)[0]
            if suggestion == secret_word:
                stats.append(turns)
                break
            # Generate feedback & filter
            feedback = get_auto_feedback(suggestion, secret_word)
            current_list = get_possible_words(current_list, suggestion, feedback)
    # Calculate & print stats
    avg = sum(stats) / len(stats)
    print("Simulation complete!")
    print("Average Turns: " + str(avg))
    print("Best Game: " + str(min(stats)) + " turns")
    print("Worst Game: " + str(max(stats)) + " turns")

# Ask number of games:
num_games = int(input("How many games in the simulation? "))
run_simulation(num_games)
