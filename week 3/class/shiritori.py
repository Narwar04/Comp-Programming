num_words = int(input())
words = [input().strip() for _ in range(num_words)]

used = set()
used.add(words[0])

for i in range(1, num_words):
    prev = words[i - 1]
    current = words[i]

    if current in used:
        print(f"Player {(i % 2) + 1} lost")
        break

    if current[0] != prev[-1]:
        print(f"Player {(i % 2) + 1} lost")
        break

    used.add(current)
else:
    print("Fair Game")