w=input()
for i in set(w):
    if w.count(i) % 2 != 0:
        result = "NO"
        break
else:
    result = "YES"

print(result)

