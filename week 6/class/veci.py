def next_permutation(arr):
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    if i == -1:
        return False

    j = len(arr) - 1
    while arr[j] <= arr[i]:
        j -= 1

    arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = reversed(arr[i + 1:])
    return True

def main():
    X = int(input().strip())

    digits = list(str(X))
    if next_permutation(digits):
        result = int(''.join(digits))
    else:
        result = 0
    print(result)

if __name__ == '__main__':
    main()

