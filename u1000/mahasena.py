input()
soldiers = list(map(int, input().split()))
print('READY FOR BATTLE' if 2 * sum(i % 2 == 0 for i in soldiers) > len(soldiers) else 'NOT READY')