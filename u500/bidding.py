for i in range(int(input())):
    a, b, c = map(int, input().split())
    print('Alice' if a > b and a > c else 'Bob' if b > c else 'Charlie')