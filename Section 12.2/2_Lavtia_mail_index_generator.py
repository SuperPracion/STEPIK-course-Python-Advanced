from string import ascii_uppercase as Letter
from random import *


def generate_index():
    return f'{choice(Letter)}{choice(Letter)}{randrange(100)}_{randrange(100)}{choice(Letter)}{choice(Letter)}'

