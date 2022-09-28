from random import *

for _ in range(int(input())):
    print(chr(randint(65, 90)) if random() > 0.5 else chr(randint(97, 122)), end='')