from math import ceil
for i in range(int(input())):
    h, x, y = map(int, input().split())
    print(ceil((h - y) / x) + 1 if h > y else 1)