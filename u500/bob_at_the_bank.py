for i in range(int(input())):
    w, x, y, z = map(int, input().split())
    print(w + (x - y) * z)