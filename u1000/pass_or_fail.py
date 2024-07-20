for i in range(int(input())):
    n, x, p = map(int, input().split())
    print('PASS' if x * 4 - n >= p else 'FAIL')