n = int(input())

total = 0.0

for i in range(n):
    q, y = map(float, input().split())
    total += q * y
print(total)