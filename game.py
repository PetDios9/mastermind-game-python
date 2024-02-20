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
        guess = input("Guess: ").strip().upper().split(' ')
        if len(guess) != CODE_LENGTH: 
            print(f"Guess is not long enough. Please guess {CODE_LENGTH} colors.")
            continue

        for color in guess:
            if color not in COLORS:
                print("One of your guesses is invalid. Please select from R, G, B, Y, W, O.")
                break
        else:
            return guess

def check_guesses(guess, real_code):
    color_count = {} 
    #y r w y y:2
    correct_guesses = 0
    incorrect_position = 0

    #added guesses to color count
    for color in real_code: 
        if color not in color_count:
            color_count[color] = 0
        color_count[color] += 1

    #check for correct position and increment correct guesses
    for guess_color, real_color in zip(guess, real_code): 
        if guess_color == real_color:
            correct_guesses += 1
            color_count[guess_color] -= 1
    #check for incorrect positions and increment incorrect position counter
    for guess_color, real_color in zip(guess, real_code):
        if guess_color != real_color and guess_color in color_count and color_count[guess_color] > 0:
            incorrect_position += 1
            color_count[guess_color] -= 1
    return correct_guesses, incorrect_position

def play_game():
    true_code = generate_color_code()
    print(f'Welcome to Mastermind. Try to crack the color code by choosing a {CODE_LENGTH} combination of the colors R, G, B, Y, W, O. You have {TRIES} tries.')
    for i in range(1, TRIES + 1):
        player_guess = guess_code()
        if player_guess == true_code: 
            print(f'You win! Code cracked in {i} tries!')
            return
        correct_guesses, incorrect_position = check_guesses(player_guess, true_code)
        print(f'Correct positions: {correct_guesses} | Incorrect positions: {incorrect_position}')
    print(f'You lost! The code was {true_code}. Better luck next time!')
play_game()