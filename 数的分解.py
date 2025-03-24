count = 0
for a in range(1, 2019 // 3 + 1):
    if '2' in str(a) or '4' in str(a):
        continue
    for b in range(a + 1, 2019 // 2):
        if '2' in str(b) or '4' in str(b):
            continue
        c = 2019 - a - b
        if c > b and '2' not in str(c) and '4' not in str(c):
            count += 1
print(count)
