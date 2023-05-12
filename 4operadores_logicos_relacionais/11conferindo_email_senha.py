''' Luiz Henrique
Operadores lógicos
AND, OR, NOT, IN e NOT IN
'''
'''
Fazer um algorítimo utilizando a condição if else e elif
exemplificando cada operação
Antes disso deve possuir um menu
Desafio Fazer um programa de login e comparar se a senha
digitada confere com a senha cadastrada e o usuário.
'''
#Solução
usuario = input('Digite o seu Usuário: ')
senha = input('Digite a sua senha: ')
usuarioBd = 'luiz'
senhaBd = '123456'
if usuario == usuarioBd and senha == senhaBd:
    print('voce está logado')
else:
    print ('você não logou')