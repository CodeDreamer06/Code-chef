for i in range(int(input())):
    x, y = map(int, input().split())
    print('Cloth' if y * 10 <= x * 100 else 'Disposable')