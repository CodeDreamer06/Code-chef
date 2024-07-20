for i in range(int(input())):
    s, x, y, z = map(int, input().split())
    print(0 if x + y + z <= s else 1 if x + z <= s or y + z <= s else 2)