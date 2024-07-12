a, b, x, y = map(int, input().split())
messi, ronaldo = a * 2 + b, x * 2 + y
print('Messi' if messi > ronaldo else 'Ronaldo' if messi < ronaldo else 'Equal')