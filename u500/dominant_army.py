for i in range(int(input())):
    print('YES' if 2 * max(a := list(map(int, input().split()))) > sum(a) else 'NO')