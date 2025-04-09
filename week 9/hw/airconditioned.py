n = int(input())
intervals = []
for _ in range(n):
    l, r = map(int, input().split())
    intervals.append((l, r))

intervals.sort(key=lambda x: (x[1], x[0]))

current_end = -1
rooms = 0

for l, r in intervals:
    if current_end >= l and current_end <= r:
        continue
    current_end = r
    rooms += 1

print(rooms)
