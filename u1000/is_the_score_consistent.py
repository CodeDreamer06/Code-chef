for i in range(int(input())):
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print('POSSIBLE' if c >= a and d >= b else 'IMPOSSIBLE')