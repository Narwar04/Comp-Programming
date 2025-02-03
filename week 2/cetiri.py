nums = list(map(int, input().strip().split()))
nums.sort()

diff1 = nums[1] - nums[0]
diff2 = nums[2] - nums[1]

if diff1 == diff2:
    print(nums[2] + diff1)
elif diff1 > diff2:
    print(nums[0] + diff2)
else:
    print(nums[1] + diff1)



