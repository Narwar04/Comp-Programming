a, d = [int(x) for x in input().split()]
asc = []
desc = []

for x in range(a):
    asc.append([float(x) for x in input().split()])

for x in range(d):
    desc.append([float(x) for x in input().split()])

total_distance = 0
total_time = 0
for x in asc:
    total_distance += x[0]
    total_time += x[1]

mid = 0
max_time = total_time
min_time = 0

while mid != (max_time + min_time) / 2:
    mid = (max_time + min_time) / 2
    completed_time = 0
    asc_distance = 0
    
    for segment in asc:
        if completed_time < mid and segment[1] + completed_time < mid:
            asc_distance += segment[0]
            completed_time += segment[1]
        else:
            asc_distance += (segment[0] / segment[1] * (mid - completed_time))
            break
    
    completed_time = 0
    desc_distance = 0
    
    for segment in desc:
        if completed_time < mid and segment[1] + completed_time < mid:
            desc_distance += segment[0]
            completed_time += segment[1]
        else:
            desc_distance += (segment[0] / segment[1] * (mid - completed_time))
            desc_distance = total_distance - desc_distance
            break
    else:
        desc_distance = total_distance - desc_distance
    
    if asc_distance == desc_distance:
        max_time = mid
    elif asc_distance < desc_distance:
        min_time = mid
    elif asc_distance > desc_distance:
        max_time = mid

print('%.5f' % mid)
