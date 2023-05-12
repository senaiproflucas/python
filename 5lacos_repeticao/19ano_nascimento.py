from datetime import date
''' Crie um programa que leia o ano de nascimento de quatro pessoas
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores'''
dataAtual = date.today().year
contJovem = 0
contAdulto = 0
for i in range(4):
    num = int(input("Digite anos de nascimento: \n"))
    if dataAtual - num >= 21:
        contAdulto += 1
    elif dataAtual - num < 21:
        contJovem += 1
print("Ao todo tivemos {} maiores e {} menores de idade.".format(
    contAdulto, contJovem))