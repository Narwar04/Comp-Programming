num_people = int(input())

pep = list(map(int,input().split()))

seen = {}
space = num_people

for index, num in enumerate(pep):
    if num in seen:
        dis = index - seen[num]
        space = min(space,dis)
        
    seen[num] = index

print(space)