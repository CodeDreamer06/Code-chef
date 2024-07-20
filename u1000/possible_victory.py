r, o, c = map(int, input().split())
print('YES' if c + 36 * (20 - o) > r else 'NO')