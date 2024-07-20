for i in range(int(input())):
    n, a, b = map(int, input().split())
    print(a * (r := n.bit_length() - 1) + (r - 1) * b)