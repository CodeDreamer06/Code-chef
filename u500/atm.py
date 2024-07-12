x, y = map(float, input().split())
print(balance if (balance := y - x - 0.5) >= 0 and x % 5 == 0 else y)