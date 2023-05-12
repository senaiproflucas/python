'''
Prof. Luiz Henrique
Importante validar tipos de variáveis para evitar possiveis erros pelo usuario para o programa não parar
o if sempre é muito utilizado para validações.
'''
nome = str(input('Olá digite o seu nome: '))
print(nome.isalpha())#retorna verdadeiro ou falso
print(nome.isdigit())#retorna verdadeiro ou falso
'''Nesse sentido é importante fazer a validação'''
if(nome.isdigit()):
    print('A variável é digito')
    print('Refaça a validação')
else:
    print(f'Olá {nome} seja bem vindo')

