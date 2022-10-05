words = 'The apple is red'.split()
result = [[w.upper(), w.lower(), len(w)] for w in words]
for i in result:
    print(i)
