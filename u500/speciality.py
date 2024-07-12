for i in range(int(input())):
    x, y, z = map(int, input().split())
    print('Setter' if x > y and x > z else 'Tester' if y > z else 'Editorialist')