for i in range(int(input())):
    print('Water filling time' if sum(map(int, input().split())) < 2 else 'Not now')