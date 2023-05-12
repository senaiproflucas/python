'''Prof. Luiz Henrique
Faça um programa que leia o ano de nascimento de um usuário e informe
de acordo com sua idade:

- Se ele ainda vai não pode dirigir
- Se é a hora de fazer o exame de direção
- Se já passou o tempo de fazer exame

Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo
'''
from datetime import datetime

dataNasc = int(input("Em qual ano você nasceu? \n"))
anoAtual = datetime.now().year
# print("Ano atual: {}".format(ano_atual))
idade = (anoAtual - dataNasc)
if idade < 18:
    print("Você tem {} anos em {} e vai e pode ter sua carteira daqui há {} anos, em {}.".format(
        idade, anoAtual, (18 - idade), (dataNasc + 18)))
elif idade > 18 and idade <=65:
    print("Você tem {} anos e já pode prestar o exame de diração.".format(idade))
    print("Você não tinha realizado o exame deveria ter realizado em: {}, há {} anos.".format(
        (dataNasc + 18), idade - 18))
else:
    print("Você tem {} anos. Agora você deverá renovar a carteira a cada 3 anos .".format(idade))