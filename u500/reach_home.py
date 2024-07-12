for i in range(int(input())):
    x, y = map(int, input().split())
    print('YES' if x * 5 >= y else 'NO')