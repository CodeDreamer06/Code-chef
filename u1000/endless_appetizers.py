from math import ceil
for i in range(int(input())):
    x, y, r = map(int, input().split())
    print(ceil((x + (r / 30)) / y))