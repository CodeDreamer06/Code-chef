from math import ceil
for i in range(int(input())):
    x, n = map(int, input().split())
    print(max(0, ceil(n / 100) - x))