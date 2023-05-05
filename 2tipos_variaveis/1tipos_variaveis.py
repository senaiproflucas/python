'''
Aula 2 Declarando variaveis e seus tipos
tipos simples: integer, float, boolean
tipos complexos: string, tuplas, listas
'''
#variáveis do tipo string
nome = str('A perereca é um ânuro')
print(nome)
#para saber o tipo da variável
print(type(nome))
#chamando a variável no print com contenação
print('O nome é: '+nome+'!')
#concatenando com print formatado
print(f'O nome é: {nome}!')
#variáveis do int
'''
integer é um tipo de variável numérica que aceita números naturais;
'''
valor = int(13)
print(valor)
#concatenado
print('O valor é:',valor,'pronto')
#print formatado
print(f'O valor é {valor} e fim')
#expressões ternárias
print('é menor')if valor < 15 else('é maior')
#variaveis do tipo float
valorFloat = float(3.5555)
print(f'O valor é {valorFloat}')
#restringindo casas decimais
print(f'O valor é {round(valorFloat,2)}')
#outra forma
print(f'O valor é com print formatado {valorFloat:.2f}')
print('O valor de print com format é {:.2f}'.format(valorFloat))

#swap trocando variáveis de valores com variável auxiliar
a = 15
b = 20
print(f'a vale {a} e b vale {b}')
c = a
a = b
b = c
print(f'a vale {a} e b vale {b}')
#ou faça esse processo
v = 5
w = 10
print(f'v vale {v} e w vale {w}')
v,w = w,v
print(f'v vale {v} e w vale {w}')
# variáveis booleanas são variáveis que trabalham com verdade ou falso
verdade = bool(True)
falso = bool(False)
print(f'{verdade} e {falso}')