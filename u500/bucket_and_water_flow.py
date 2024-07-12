for i in range(int(input())):
    w, x, y, z = map(int, input().split())
    print('Unfilled' if x > (v := w + y * z) else 'Filled' if x == v else 'Overflow' )