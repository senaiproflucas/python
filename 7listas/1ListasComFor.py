'''
Listas com Python
fatiamento
append, insert, pop, del, clear, extend
'''
#         0    1    2    3
lista = ['A', 'B', 10.4, 'D']
#         -4   -3   -2   -1
string = 'Atack on Titan'
print(lista[2])
print(lista[0:2])
print(lista[0:3:2])
print(string[2])

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(lista1)
lista1.extend(lista2)
lista1.append('b')
lista1.insert(0, 'Banana')
print(lista1)
lista1 = list(range(0, 100, 8))#cria a função list e
print(lista1)           #a função range deixa os valores iteráveis
print(min(lista1))      #porque são iteráveis
print(max(lista1))
print(lista2)
#lista2.pop()#remove último elemento
#del(lista2[3:5])
print(lista2)
print(lista3)

lista3 = list(range(0, 20, 2))
soma = 0
for valor in lista3:
    print(valor)
    soma += valor
    print(soma)

l2 = [4, 'luiz', 2.5, 'adriano', True, False]
for elem in l2:
    print(f'O tipo é {type(elem)} e o valor é {elem}')
