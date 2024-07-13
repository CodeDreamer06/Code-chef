from math import ceil
for i in range(int(input())):
    n, x = map(int, input().split())
    print(max(0, ceil(((n - x) / 4))))