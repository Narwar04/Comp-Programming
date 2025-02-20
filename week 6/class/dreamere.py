import itertools
from datetime import datetime

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def valid_date(dd, mm, yyyy):
    try:
        date = datetime(yyyy, mm, dd)
        return date >= datetime(2000, 1, 1)
    except ValueError:
        return False

def find_dates(digits):
    digits = list(map(int, digits.replace(' ', '')))
    possible_dates = set()
    for perm in itertools.permutations(digits):
        dd, mm, yyyy = int(''.join(map(str, perm[:2]))), int(''.join(map(str, perm[2:4]))), int(''.join(map(str, perm[4:])))
        if valid_date(dd, mm, yyyy):
            possible_dates.add((dd, mm, yyyy))
    return possible_dates

def main():
    t = int(input())
    for _ in range(t):
        digits = input().strip()
        possible_dates = find_dates(digits)
        if possible_dates:
            earliest_date = min(possible_dates, key=lambda date: datetime(date[2], date[1], date[0]))
            print(len(possible_dates), f"{earliest_date[0]:02d} {earliest_date[1]:02d} {earliest_date[2]}")
        else:
            print(0)

if __name__ == "__main__":
    main()