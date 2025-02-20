import bisect

N, H = map(int, input().split())

stalacite = []
stalagmite = []

for x in range(N):
    height = int(input())
    if x % 2 == 0:
        stalagmite.append(height)
    else:
        stalacite.append(H - height)

stalacite.sort()
stalagmite.sort()

len_stalacite = len(stalacite)
len_stalagmite = len(stalagmite)

min_obstacles = N
count = 0

for x in range(1, H + 1):
    obstacles = (len_stalagmite - bisect.bisect_left(stalagmite, x)) + bisect.bisect_left(stalacite, x)
    
    if obstacles == min_obstacles:
        count += 1
    elif obstacles < min_obstacles:
        min_obstacles = obstacles
        count = 1

print(min_obstacles, count)
