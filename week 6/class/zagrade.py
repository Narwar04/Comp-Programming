orig = input()

stack = []
pos = []
for i, ch in enumerate(orig):
    if ch == '(':
        stack.append(i)
    elif ch == ')':
        loc = stack.pop()
        pos.append((loc, i))

print(pos)

for i in range(1, 1 << (len(pos))):
    block = set()
    for j in range(len(pos)):
        if i & (1 << j) != 0:
            a, b = pos[j]
            block.add(a)
            block.add(b)
    print(block)