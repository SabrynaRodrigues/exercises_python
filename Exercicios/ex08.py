lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i','j','k']
for i, v in enumerate(lista):
# i for indice and v for valor
    if i <= 5:
        continue
    else:
        print(v)