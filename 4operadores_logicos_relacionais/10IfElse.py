'''
*Condições If Elif e Else
*Executa comparações e a partir das comparações se tem um resulta
*do

*Fazer a brincaderia do:
if true:
    print('verdadeiro')
    Else:
    print(false)
'''

'''
Operadores Relacionais
==, <, <=, >, >=, !=
'''
'''
Condições Lógicas: AND, OR, NOT, IF
'''
'''nome = input('Qual é o seu nome: ')
idade = input('Qual é a sua idade: ')#string
#Limite para pegar empréstimo
idade = int(idade)#cast
idadeMenor = 18 #muito Jovem
idadeMaior = 30 #passou da idade
if idade >= idadeMenor and idade <= idadeMaior:
    print(f'{nome} pode pegar o empréstimo com juros de 3,5% a.a.')
else:
    print(f'{nome} não pode pegar o empréstimo a 3.5% a.a.')
'''
'''
nome = input('Qual é os eu nome: ')
num1 = input('digite a valor 1: ')
num2 = input('digite o valor 2: ')
num1 = int(num1)
num2 = int(num2)
print(type(num1))
resultado = 0
if num1 < num2:
    resultado = num1 + num2
    print (f' O resultado é: {resultado}')
elif num1 == num2 :
    resultado = num1 * num2
    print (f'O resultado é: {resultado}')
else:
    r = num1 - num2
    print(f'O resultado é {resultado}')
'''
'''
nome = input('Escreva o seu nome: ')
idade = input ('Escreva sua idade: ')
idade = int(idade)
if(idade <= 4):
    print(f'{nome} é bebê {idade}')
elif(idade >=5 and idade <=11):
    print(f'{nome} é criança {idade}')
elif(idade >=12 and idade<=17 ):
    print(f'{nome} é adolescente {idade}')
elif(idade >=18 and idade <=64):
    print(f'{nome} é adulto {idade}')
else:
    print(f'{nome} é idoso {idade}')
'''
try: #Não deixa o usuário digitar caractere
    idade1 = int(input('digite o valor 1:  '))
    idade2 = int(input('Digite o valor 2: '))
    if(idade1 == idade2):
        print(f'As idades são Iguais {idade1}')
    else:
        print(f'Possuem idades diferentes {idade1} e {idade2}')
except:
    print('ERROR')
#Pass e Elipsis serve para deixar a condição em branco e depois editar

nome = False
if nome == True:
    ... #pode usar o False
else:
    print('tchau')