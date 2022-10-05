a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]

for i in a:
    if i in b:
        print(i)
    else:
        print(f'{i}: valor presente somente em uma lista.')
