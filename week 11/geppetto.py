from collections import defaultdict

n, m = map(int, input().split())

invalid_combinations = defaultdict(set)
for _ in range(m):
    a, b = sorted(map(int, input().split()))
    invalid_combinations[a].add(b)

stack = [(n, [])]
total_ways = 0

while stack:
    current, chosen = stack.pop()

    if current == 0:
        total_ways += 1
        continue

    stack.append((current - 1, chosen))

    current_is_valid = True
    for value in invalid_combinations[current]:
        if value in chosen:
            current_is_valid = False
            break

    if current_is_valid:
        stack.append((current - 1, chosen + [current]))

print(total_ways)

