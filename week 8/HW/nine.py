T = int(input())
for i in range(T):
    numberOfNoNine= 8 * pow(9, int(input())-1, 1000000007)
    print (numberOfNoNine % 1000000007)