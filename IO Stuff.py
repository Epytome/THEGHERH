with open('words_alpha.txt', 'r') as f:
    words = f.read().splitlines()


count = 0
for w in words:
    if w[-1] == 's':
        count += 1

print(count)




count = 0
a = 0
for w in words:
    if "q" in w and "qu" not in w:
        count += 1

print(count)
