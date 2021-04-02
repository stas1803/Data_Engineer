src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

next_big = []
prev = 0
for i in src:
    if i > prev:
        next_big.append(i)
        prev = i
    else:
        prev = i

print(next_big)