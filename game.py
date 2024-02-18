import random

COLORS = ['R', 'G', 'B', 'Y', 'W', 'O']
TRIES  = 10
CODE_LENGTH = 4

def generate_color_code():
    code = []
    for i in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    return code

def guess_code():
    while True:
        guess = input("Guess: ").upper().split(' ')

        if len(guess) != CODE_LENGTH: 
            print(f"Guess is not long enough. Please guess {CODE_LENGTH} colors.")
            continue

        for color in guess:
            if color not in COLORS:
                print("One of your guesses is invalid. Please select from R, G, B, Y, W, O.")
                break
        else:
            break

        return guess

def check_guesses(guess, real_code):
    color_count = {}
    correct_guesses = 0
    incorrect_position = 0

    #added guesses to color count
    for guess in guess: 
        if guess not in color_count:
            color_count[guess] = 1
        else:
            color_count[guess] += 1

    #check for correct position and increment correct guesses
    for guess_color, real_color in zip(guess, real_code): 
        if guess_color == real_color:
            correct_guesses += 1
            color_count[guess_color] -= 1
    #check for incorrect positions and increment incorrect position
    for guess_color, real_color in zip(guess, real_color):
        if guess_color in color_count and color_count[guess_color] > 0:
            incorrect_position += 1
            color_count[guess_color] -= 1

    return correct_guesses, incorrect_position