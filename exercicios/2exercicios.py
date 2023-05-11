'''
Faça um programa que peça ao usuário digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não
digite um número inteiro, informe que não é um número inteiro.
'''
#Solução

num1 = input('Digite um número: ')
if (num1.isdigit()) :
    num1 = int(num1)
    r = num1%2
    if(r==0):
        print('O número {0} é par {1}'.format(num1, r))
    else:
        print('O número {0} é ímpar {1}'.format(num1, r))
else:
    print('Digite um valor válido')

'''
Faça um programa que pergunte a hora ao usuário e, 
baseando-se no horário descrito, exiba a saudação apropriada. ex.: Bom 
dia 0-11, Boa tarde 12-17 e Boa noite 18-23
'''
hora = int(input('Olá Digite a Hora: '))
minuto = int(input('Digite o Mínuto: '))
if (hora >=0 and hora <=11) :
    print('Bom dia!!!')
elif (hora >11 and hora<=17 and minuto <=59) :
    print('Boa tarde!!!')
else:
    print('Boa noite!!! ')
'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver
 4 letras ou menos escreva “Seu nome é Curto”; se tiver entre 5 e 6 letras, 
escreva “seu nome é médio”; maior que 6 escreva “Seu nome é extenso
'''
usuario = input('Digite o seu nome: ')
qtCaractere = len(usuario)
if(qtCaractere<=4):
    print('Seu nome é curto')
elif (qtCaractere<=7):
    print('Nome médio')
else:
    print ('Nome extenso')

