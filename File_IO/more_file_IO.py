import os
import random

path = "data"

file_names = os.listdir(path)

for i,f in enumerate(file_names):
    print(str(i) + ") " + f)

choice = input('Pick one ')
choice = int(choice)

file = path + "/" + file_names[choice]
print (file)

with open(file, 'x') as f:
    lines = f.read().splitlines()

print(lines)

category_name = lines[0]
puzzle = random.choice( lines[1:] )

print(category_puzzle)
print(puzzle)
