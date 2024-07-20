from itertools import combinations
for i in range(int(input())):
    w, x, y, z = map(int, input().split())
    print('YES' if any(sum(j) == w for i in range(1, 4) for j in combinations((x, y, z), i)) else 'NO')