
test = int(input())  
for i in range(test):
    num_dolls = int(input())
    dimensions = list(map(int, input().split()))  
    lis_length = 0 
    dp = [0] * num_dolls 
    
    sorted_dolls = sorted((dimensions[i], -dimensions[i + 1]) for i in range(0, 2 * num_dolls, 2))

    for i, neg_height in sorted_dolls:
        height = -neg_height  # Convert back to positive height
        low, high = 0, lis_length

        while high > low:
            mid = (low + high) // 2
            if dp[mid] < height:
                high = mid
            else:
                low = mid + 1

        dp[low] = height  
        if low == lis_length:
            lis_length += 1  
    print(lis_length)  