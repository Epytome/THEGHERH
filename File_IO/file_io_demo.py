import math
import random

with open('scrabble_words.txt', 'r') as f:
    words = f.read().splitlines()




count = 0
for i in range(1, 1000000000):
    if (i % 19 == 0) and (i % 5 == 0) :
        count += 1

print(count)
