'''
idade version 2
faça um programa que o usuário digite o nome, o sexo, a sua data de nascimento e calcule quantos anos ele possui
o programa deverá exibir a idade, se o uruário pode dirigir se for mulher se já está na idade de mamografia
se for home se está na idade de fazer exame de próstata.
'''
import datetime

nome = (str(input('Olá Digite seu nome: ')))
diaNasc = int(input('Digite o dia do seu nascimento: '))
mesNasc = int(input('Digite o mes do seu nascimento: '))
anoNasc = int(input('Digite o ano do seu nascimento: '))
data = datetime.date.today()
dataD = data.day
dataM = data.month
dataA = data.year
idade = (dataA - anoNasc)
print(f'A idade é {idade}')
if ((dataD < diaNasc and dataM <= mesNasc)):
    idade = idade -1
    print(f'Olá {nome} sua idade é {idade}')
elif (dataD == diaNasc and mesNasc == dataM):
    print(f'Parabéns {nome} e feliz aniverssario sua idade hoje é {idade}')
else:
    print(f'Olá {nome} sua idade é {idade}')

