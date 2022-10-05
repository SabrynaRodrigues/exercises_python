# Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo.
list1 = [0, 1, 2, 3, 4]

#main
def quadrado(x):
    return x**2


def cubo(x):
    return x**3


both = [quadrado, cubo]

# programa
for i in list1:
    valor = map(lambda x: x(i), both)
    print(list(valor))