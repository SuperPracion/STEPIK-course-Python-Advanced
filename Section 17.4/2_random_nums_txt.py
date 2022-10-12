import random

with open('random.txt', 'w', encoding='utf-8') as file:
   for _ in range(25):
      print(random.randint(111, 777), file=file)