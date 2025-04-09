from collections import Counter

def smallest_missing_number(digits):
    counts = Counter(digits)
    num = 1
    while True:
        required = Counter(str(num))
        for d in required:
            if counts.get(d, 0) < required[d]:
                return num
        num += 1

n = input().strip()
print(smallest_missing_number(n))
