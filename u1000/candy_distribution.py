for i in range(int(input())):
    n, m = map(int, input().split())
    print('YES' if n % m == 0 and n / m % 2 == 0 else 'NO')