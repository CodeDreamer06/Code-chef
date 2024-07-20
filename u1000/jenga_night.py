for i in range(int(input())):
    n, x = map(int, input().split())
    print('YES' if x % n == 0 else 'NO')