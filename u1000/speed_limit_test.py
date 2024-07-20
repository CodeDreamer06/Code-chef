for i in range(int(input())):
    a, x, b, y = map(int, input().split())
    print('Alice' if a * y > b * x else 'Bob' if a * y < b * x else 'Equal')