n = int(input())
s = input().strip()
arr = list(map(int, input().split()))

people = []
for i in range(n):
    people.append({'gender': s[i], 'skill': arr[i], 'pos': i + 1})

current_people = people.copy()
result = []

while True:
    candidates = []
    for i in range(len(current_people) - 1):
        a = current_people[i]
        b = current_people[i + 1]
        if a['gender'] != b['gender']:
            diff = abs(a['skill'] - b['skill'])
            candidates.append((i, diff, a['pos'], b['pos']))

    if not candidates:
        break

    min_diff = min(c[1] for c in candidates)
    filtered = [c for c in candidates if c[1] == min_diff]
    selected = min(filtered, key=lambda x: x[0])

    result.append((selected[2], selected[3]))

    i = selected[0]
    current_people = current_people[:i] + current_people[i + 2:]

print(len(result))
for pair in result:
    print(pair[0], pair[1])
