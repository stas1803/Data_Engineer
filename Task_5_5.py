src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

uniq_src = set()
tmp = set()
for i in src:
    if i not in tmp:
        uniq_src.add(i)
    else:
        uniq_src.discard(i)
    tmp.add(i)

result = [i for i in src if i in uniq_src]
print(result)