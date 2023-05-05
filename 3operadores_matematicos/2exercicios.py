import datetime
'''
Exercícios
1 fazer um programa que peça o nome do usuário e a data de nascimento através da data do sistema já dizer a idade.
2A fazer um programa que calcule o juros simples. Paulo quer abrir um negócio junto com Mário fizeram um empréstimo
 e agora possuem um capital de R$ 10850, com uma taxa de 3% ao mês pelo período de 1 ano.
2B Faça o mesmo programa só que agor ao cliente pode digitar os valores a taxa e o tempo.
3 fazer um programa que calcule a área de um triângulo equilátero com a base de 8m e altura de 20m
4 Mario pegou R$248,00 da bolsa de Anita sendo que ela tinha R$950,00. Faça um programa que calcule a porcentagem.
5 18 anos são as idades de Ana e Laura somadas há dez anos, Ana é 2 anos mais velha que Laura. 
Qual é a idade de Laura nos dias de hoje? Faça um programa que calcule as idades.
'''
import datetime

#1
nome = str(input('Olá digite seu nome: '))
data = datetime.date.today()
diaD = data.day
mesD = data.month
anoD = data.year
dataDia = int(input('Digite o dia do seu nascimento: '))
dataMes = int(input('Digite o mes do seu nascimento: '))
dataAno = int(input('Digite o ano do seu nascimento: '))
print('O cálculo será com base somente no ano e não será levado em conta o dia e o mês')
idade = data.year - dataAno
print(f'Olá {nome} e você tem {idade} anos de idade!')