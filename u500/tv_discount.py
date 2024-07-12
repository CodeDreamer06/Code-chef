for i in range(int(input())):
    a, b, c, d = map(int, input().split())
    print('First' if a - c < b - d else 'Second' if a - c > b - d else 'Any')