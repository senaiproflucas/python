'''
Elabore um programa que o usuário digite um valor e o sistema calcula quando um valor é maior ou menor
'''
n1 = int(input('Digite a nota1: '))
n2 = int(input('Digite a nota2: '))
if (n1>n2):
    print(f'{n1} é] maior que {n2}')
elif (n1<n2):
    print(f'{n1} é menor que {n2}')
else:
    print(f'{n1} é igual a {n2}')