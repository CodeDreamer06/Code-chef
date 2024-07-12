for i in range(int(input())):
    pay = input().split()
    print('YES' if int(pay[0]) >= int(pay[1]) else 'NO')