t = (1, 2, 3, 4, 1, 2, 3, 1, 2, 1)
idx = 2
find = 2
for x in t[idx:]:
    if x == find :
        print(idx)
        break
    idx = idx + 1