n, k = map(int, input().split())
print(sum([int(input()) % k == 0 for i in range(n)]))