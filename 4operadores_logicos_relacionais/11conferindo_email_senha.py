'''
Operadores lógicos
AND, OR, NOT, IN e NOT IN
'''
'''
Fazer um algorítimo utilizando a condição if else e elif
exemplificando cada operação
Antes disso deve possuir um menu
'''
'''
Desafio Fazer um programa de login e comparar se a senha
digitada confere com a senha cadastrada e o usuário.
'''
#Solução
usuario = input('Digite o Usuário: ')
senha = input('Digite a senha: ')
usuarioBd = 'luiz'
senhaBd = '123456'
if usuario == usuarioBd and senha == senhaBd:
    print('voce está logado')
else:
    print ('você não logou')
'''
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
idade = int(idade)
if idade < 18:
    print(f'{nome} a sua idade é: {idade}, você é menor de idade')
elif idade>=18 and idade <30:
    print(f'{nome} a sua é: {idade} e você é maior de idade')
elif idade >= 30 and idade <= 39:
    print(f'{nome} sua idade é {idade} e você já é senhor')
else:
print(f'{nome} Errou')
'''