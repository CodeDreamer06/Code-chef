for i in range(int(input())):
    p = list(map(int, input().split()))
    print('YES' if 2 * max(p) > sum(p) else 'NO')