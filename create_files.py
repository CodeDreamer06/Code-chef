questions = '''
'''
for i in questions.splitlines():
    if not i.isnumeric():
        open('/' + i.lower().replace(' ', '_') + '.py', 'w').close()
