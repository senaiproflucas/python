'''Prof. Luiz Henrique
Calculando números pares e números ímpares. Se for par escrever em azul e se for ímpar escrever em verde
'''
n = int(input('Digite o número: '))
if (n%2 == 0):
    print(f'\033[34m O número {n} é par \033[0m')
else:
    print(f'\033[32m O número {n} é ímpar \033[0m')
