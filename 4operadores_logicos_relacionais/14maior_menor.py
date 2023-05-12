''' Faça um programa que leia a nota de quatro pessoas
No final, mostre qual foi a maior e a menor nota lidas'''

notaMaior = 0
notaMenor = 0

for i in range(1, 5):
    nota = float(input("Digite um nota: \n"))
    if i == 1:
        notaMaior = nota
        notaMenor = nota
    else:
        if nota > notaMaior:
            notaMaior = nota
        elif nota < notaMenor:
            notaMenor = nota

print("O maior peso é {}kg".format(notaMaior))
print("O menor peso é {}kg.".format(notaMenor))