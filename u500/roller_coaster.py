for i in range(int(input())):
    ride = input().split()
    print('YES' if int(ride[0]) >= int(ride[1]) else 'NO')