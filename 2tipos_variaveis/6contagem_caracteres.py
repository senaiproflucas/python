'''
Prof. Luiz Henrique
Função len é uma funçaõ importante que permite saber o tamanho de
uma variável através da contagem de seus caracteres.
'''
nUser = input('Digite o usuário: ')
quantString = len(nUser)
if quantString <8:
    print(f'Digte até 8 caracteres')
else:
    print(f'Acesso autorizado')
alpha1 = input('Digite algo: ')
alpha2 = input('Digite algo a mais: ')
print(f'A soma dos caracteres é: {len(alpha1) + len(alpha2)} ')
print (alpha2.__len__()) # alpha2.chama o método __len__
'''
Funções são métodos e ele é chamado (invocado)
em qualquer parte do código, nas aulas seguintes
veremos isso na parte de orietnação a objetos POO
Mas o método nada mais é do que uma peça de quebra
cabeça que se encaixa e executa o que é ordenado.
No python existem muitas bibliotecas com vários métodos
como por exemplo a biblioteca Math, Emoji, entre outras.
'''


