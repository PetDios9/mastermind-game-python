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
