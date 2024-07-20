p1 = p2 = lead = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    p1 += a
    p2 += b
    if abs(p1 - p2) > abs(lead):
        lead = p1 - p2
print(1 if lead > 0 else 2, abs(lead))