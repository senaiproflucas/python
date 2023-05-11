nome = "gabriel"
idade = 25
peso = 89.0
altura = 1.82
imc = (peso/(altura**2))
'''Objetivo da aula imprimir resultados de maneira mais simples, declarar variáveis
em meio a um print
Competencias Saber imprimir com duas casas decimais, e formas simples de impressão
Habilidades: saber utlizar diversos tipos de print.'''
print("O ", nome, "tem ", idade," idade ", "com peso de ",+
      peso, "altura de ", altura, "E o imc é: ", imc)
#outra forma de imprimir é com o f string
print(f"{nome} tem {idade} anos de idade {peso} kg "
      f"{altura} altura e imc {imc:.2f}")
'''
Este print fica mais dinâmico, não tem que ficar inserindo tantas
vírgulas.
para deixar a variavel com duas casas decimais usar o comando
:.2f no lugar da variável a ser impressa
'''
#outra forma de print
print("{0} tem {1} anos de idade {2} kg{3} altura e "
      "imc {4:.2f}".format(nome, idade, peso, altura, imc))
'''
nesse caso leger as variáveis no final utilizando o .format e as variáveis
a ordem sempre será 0 1 2 3 4...10 pode-se escolher qual variável vem primeiro
no meio das chaves.
'''
#declaração de variaveis

print("{n} tem {i} anos h: {h} kg{k} altura e imc {im:.2f}".format(n=nome, i=idade,k=peso, h=altura, im=imc))
'''
nesse modelo de print usa o .format e declara novas vairáveis.
'''

'''
Ao aluno: Essa aula foi pensada com bastante carinho e cuidado para que você não erre
saiba utilizar com sabedoria seus códigos.
Vocês ainda estão no inicio, não desanimem na vida existem diversos desafios e nós seres
vivos temos a obrigação de superá-los, sendo esse um mecanismo invevitável da vida.
'''



nome = 'luiz'
num1 = 10
num2 = 5.5
r = num1+num2

print(f'{nome} o resultado é {r:.2f}')
print('{0} o resultado é {1:.2f}'.format(nome, r))

a = '10'
a = int(a)
r = a*10
r = str(r)
print(f'{r}',type(r))