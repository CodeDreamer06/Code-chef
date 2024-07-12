for i in range(int(input())):
    x, y = map(int, input().split())
    print('PROFIT' if y > x else 'NEUTRAL' if y == x else 'LOSS')