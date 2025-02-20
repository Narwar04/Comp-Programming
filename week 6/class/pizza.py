from collections import defaultdict

def findCombos(current, restrCombos, Chosen):
    if current == 0:
        return 1
    total = 0
    goodCombo = True

    for value in restrCombos[current]:
        if value in Chosen:
            goodCombo = False

    total += findCombos(current - 1, restrCombos, Chosen)

    if goodCombo:
        total += findCombos(current - 1, restrCombos, Chosen + [current])

    return total

N, M = map(int, input().split())
restrCombos = defaultdict(set)

for _ in range(M):
    a, b = sorted(map(int, input().split()))
    restrCombos[a].add(b)

total = findCombos(N, restrCombos, [])
print(total)
