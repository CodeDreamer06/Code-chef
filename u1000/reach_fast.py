from math import ceil
for i in range(int(input())):
    a, b, k = map(int, input().split())
    print(ceil(abs(a - b) / k))