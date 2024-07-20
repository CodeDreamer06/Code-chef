from math import sqrt, floor
for i in range(int(input())):
    n = int(input())
    print('no' if any(n % i == 0 for i in range(2, floor(sqrt(n)) + 1)) or n == 1 else 'yes')