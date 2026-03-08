def load_all_words (filename):
    # Tries to open file
    try:
        with open(filename, 'r') as file:
           # If file found, returns a full array
           return [line.strip().lower() for line in file.readlines()]
    except FileNotFoundError:
        print("The file is not found.")
        # If file not found, returns a blank array
        return []