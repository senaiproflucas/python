from math import ceil
from math import floor


'''
Realizando leitura de uma variável
é quando o usuário pode inserir valores em uma variável via teclado
esse tipo de entrada é string, em algumas linguagens é necessário converter a variável para seu tipo
no python ele converte de forma altomática.
Outro aspecto importante é fazer o tratamento do que foi digitado através de funções
para tirar espaços em branco entre o que foi digitado, da esquerda, da direita e do meio.
para saber o tamanho, tipo, para inserir casas decimais, arredondar para cima, para baixo, entre outros.

O comando input é o que fara a variável ser lida pelo teclado

'''
nome = input(str('Olá digite o seu nome: '))
print(f'Olá {nome} seja bem vindo')
#tratamento de variáveis dá para forçar deixar todas as primeiras letras em maiúsculas?
#o ponto . ele chama o método é como um encaixe que se faz.
#caso a função fique dentro do parênteses ele fara o tratamento no que foi escrito, fora de tudo ele trabalha
#sobre a variável nome
nome = input(str('Olá digite seu nome novamente: ')).capitalize()
print(f'Olá {nome} seja bem vindo')
#1 faça um programa em que todas as letras fiquem maiúsculas, quando digitada na variável.
#2 faça um programa em que todas as letras fiquem somente com a primeira letra maiúscula ao digitar
#3 faça um programa em que todas as letras fiquem minúsculas.
#4 faça um programa em que se digite um número real em uma variável float em que substitui . por ,
#5 faça um programa que arredonde um valor do tipo float para cima
#6 faça um programa que arredonde um valor do tipo float para baixo
#7 faça um programa que tire os espaços da esquerda de uma digitação
#8 faça um programa que tire os espaços da direita de uma digitação
#9 faça um programa que tire os espaços internos de uma digitação
#respostas



#1
nome = str(input('Olá digite seu nome: ')).upper()
print(f'Olá {nome} bom dia!')
#2
nome = str(input('Olá digite seu nome: ')).capitalize()
print(f'Olá {nome} bom dia!')
#3
nome = str(input('Olá digite seu nome: ')).lower()
print(f'Olá {nome} bom dia!')
#4 para esse fazer conversão de variáveis
num = str(input('Olá digite um número real: ')).replace(",",".")
num = float(num)#converter para o tipo de variável float
print(f'O número digitado foi {str(num).replace(".",",")}')#converter para string novamente
#5 para esse exercício importar a biblioteca math
num = str(input('Olá digite um número real: ')).replace(",",".")
num = float(num)
print(floor(num))
#6 para esse exercício importar a biblioteca math
num = str(input('Olá digite um número real: ')).replace(",",".")
num = float(num)
print(ceil(num))
#arredondar para cima ou para baixo
num = str(input('Olá digite um número real: ')).replace(",",".")
num = float(num)
print(round(num))
#7
frase = str(input('Olá digite seu nome: ')).lstrip()
print(f'Olá {frase} bom dia!')
#8
frase = str(input('Olá escreva uma frase: ')).rstrip()
print(f'Olá {frase} bom dia!')
#9
frase = str(input('Olá escreva uma frase: ')).strip()
print(f'Olá {frase} bom dia!')
#11 faça um programa que retire os espaços entre as letras
frase = str(input('Olá escreva uma frase: ')).split()
print(f'Olá {frase} bom dia!')
#12 faça um programa em que as letras maiúsculas fiquem minúsculas e ao contrário swapcase().
nome = str(input('Olá escreva uma frase: ')).swapcase()
print(f'Olá {nome} bom dia!')




