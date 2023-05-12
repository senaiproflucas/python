''' Programa que irá pedir para que o usuário digite as bases decimais:
1 para binário
2 para octal
3 para hexadecimal
'''
num = int(input("Digite um número a ser convertido: \n"))
base = int(input('''Escolha a base da conversão:
Para binário digite: 1
Para octal digite: 2
Para hexadecimal digite: 3
Escolha: \n'''))

if base == 1:
    print("Você escolheu binário.")
    print(f"{num} convertido para binário é: {bin(num)[2:]}.")
elif base == 2:
    print("Você escolheu octal.")
    print(f"{num} convertido para a base octal é: {oct(num)[2:]}.")
elif base == 3:
    print("Você escolheu hexadecimal.")
    print("{num} convertido para hexadecimal é: {hex(num)[:2]}.")
else:
    print("Escolha apenas uma das 3 opções.")