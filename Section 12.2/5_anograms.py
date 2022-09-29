from random import *

word = list(input())
shuffle(word)
print(*word, sep='')