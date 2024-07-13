for i in range(int(input())):
    x, y = map(int, input().split())
    print('BIKE' if x < y else 'CAR' if x > y else 'SAME')