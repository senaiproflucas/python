''' Prof. Luiz Henrique
Crie um programa que leia dois valores e mostre um menu
na tela:

1: somar
2: multiplicar
3: maior
4: novos números
5: sair do programa

Seu programa deverá realizar a operação solicitada em cada caso '''

num1 = float(input("Digite um número (1/2): \n"))
num2 = float(input("Digite outro número (2/2): \n"))
menu = (
'''\nMENU PRINCIPAL:
[1] soma
[2] multiplicação
[3] maior ou menor
[4] escolher novos números
[5] encerrar o programa\n '''
)
maior = 0
menor = 0

print(menu)

menu = int(input("Sua escolha [opções de 1 a 5]: \n"))
while menu != 5:
    if menu > 5:  # exceção maior
        print("Escolha um número de 1 a 5.")
        menu = int(input("Sua escolha: \n"))
    elif menu < 0:  # exceção menor
        print("Warning: escolha um número positivo.")
        menu = int(input("Sua escolha: \n"))
    else:  # Acionamento normal do programa:
        if menu == 1:  # Soma:
            print("Vocẽ escolheu soma!")
            print("Resultado da soma: \n{} + {} = {}".format(num1, num2, (num1 + num2)))
            print(menu)
            menu = int(input("Sua escolha: \n"))
        elif menu == 2:  # Multiplicação:
            print("Você escolheu multiplicação!")
            print("Resultado da multiplicação: \n{} x {} = {:.0f}".format(num1, num2, (num1 * num2)))
            print(menu)
            menu = int(input("Sua escolha: \n"))
        elif menu == 3:  # Maior ou menor:
            if num1 > num2:
                maior = num1
                menor = num2
                print("O maior é {} e o menor é {}.".format(maior, menor))
                print(menu)
            elif num2 > num1:
                maior = num2
                menor = num1
                print("O maior é {} e o menor é {}.".format(maior, menor))
                print(menu)
            else:
                print("Os dois números são idênticos.")
                print(menu)
            menu = int(input("Sua escolha: \n"))
        elif menu == 4:  # Novos números:
            numeroNovo1 = float(input("Novo número 1: \n"))
            numeroNovo2 = float(input("Novo número 2: \n"))
            num1 = numeroNovo1
            num2 = numeroNovo2
            print(menu)
            menu = int(input("Sua escolha: \n"))
print("Opção 5: programa encerrado.")