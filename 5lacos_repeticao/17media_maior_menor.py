''' Prof. Luiz Henrique
Crie um programa que leia vários números inteiros pelo teclado
No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lidos
O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores
'''

flag = False
cont = soma = resultado = maior = menor = 0

while flag == False:
    n = int(input("Digite um número inteiro: \n"))

    #  Média:
    soma += n
    cont += 1
    resultado = (soma / cont)

    #  Maior/Menor:
    if n > maior:
        maior = n
    if menor == 0:
        menor = n
    if n < menor:
        menor = n

    #  Continuação:
    cont = str(input("Quer continuar? [SIM / NÃO] \n")).strip().upper()
    if cont == "NÃO":
        flag = True

print("Média: {:.1f}".format(resultado))
print("Maior: {} | Menor: {}".format(maior, menor))