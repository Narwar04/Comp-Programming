from collections import Counter
import re

(x, n), y = input().split(), input()


def add_ones(form):
    lis = []
    for i,c in enumerate(form):
        lis.append(c)
        if not c.isnumeric() and (i == len(form) - 1 or not form[i+1].isnumeric()):
            lis.append('1')
    return ''.join(lis)

def ingredient(form):
    c = Counter()
    for a, b in re.findall(r"([A-Z]+)([0-9]+)", add_ones(form)):
        c[a] += int(b)
    return c

def create(x,y,n):
    total = 2147483647
    for k,v in y.items():
        total = min(total, (x[k]*n) // v)
    return total

print(create(ingredient(x), ingredient(y), int(n)))
