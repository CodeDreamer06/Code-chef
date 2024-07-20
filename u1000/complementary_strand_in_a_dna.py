c = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

for i in range(int(input())):
    input()
    print(''.join([c[i] for i in input()]))