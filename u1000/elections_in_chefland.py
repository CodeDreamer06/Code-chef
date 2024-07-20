for i in range(int(input())):
    n, x = map(int, input().split())
    print(sum(i >= x for i in map(int, input().split())))