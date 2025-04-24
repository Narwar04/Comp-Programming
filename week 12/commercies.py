n, p = map(int, input().split())
a = list(map(int, input().split()))
b = [x - p for x in a]

max_ending_here = max_so_far = b[0]
for x in b[1:]:
    max_ending_here = max(x, max_ending_here + x)
    max_so_far = max(max_so_far, max_ending_here)

print(max(0, max_so_far))
