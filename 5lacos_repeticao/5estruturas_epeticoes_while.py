'''Prof. Luiz Henrique

Condição While
while continue
while break
'''
n1 = 0
while n1 < 10:

    n1 += 1
n2 = 0
while n2 < 10:
    n2 += 1
    print(n2)
    continue
coluna = 0
while coluna <10:
    coluna += 1
    print(coluna)
    linha = 0
    while linha < 5:
        linha += 1
        print(f'{coluna},{linha}')

while True:
    num1 = input('Digite o primeiro número: ')
    num2 = input ('Digite o segundo número: ')
    operador = input('Digite o operador')

    if not num1.isnumeric() or not num2.isnumeric() :
        print('Digite um número: ')
        continue
    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        print(num1+num2)
    elif operador == '-':
        print(num1-num2)
    elif operador == '*':
        print(num1*num2)
    elif operador == '/':
        print(num1/num2)
        sair = input('Deseja sair? [s] [n]: ')
        if sair == 's':
            break
    else:
        print('Operador Invalido')



