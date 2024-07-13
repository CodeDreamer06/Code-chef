from math import ceil
for i in range(int(input())):
    n, x = map(int, input().split())
    print(ceil(n / 6) * x)