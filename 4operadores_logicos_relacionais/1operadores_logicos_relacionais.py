'''
Condicional if trablaha com comparações
Se tal número é maior que outro então faça isso SENÃO faça aquilo
como fazer isso no algorítmo
Operadores relacionais
maior >
maior ou igual >=
menor <
menor ou igual <=
igual ==
diferente !=
Operadores lógicos
ou
e
não ou
não e
tabela verdade

p   q   ou  e
v   v   v   v
v   f   v   f
f   v   v   f
f   f   f   f

'''
a = 15
b = 14
print(a<b)
#if é um condicional de comparação sempre terá uma saída True ou False
#sempre necessário trabalhar com a indentação;
if(a>b):
    print('a é maior que b')
else:
    print('a é menor que b')
#outro exemplo
'''
Operadores matemáticos
soma +
subtração -
divisão /
multiplicação *
resto da divisao %
quociente //
exponenciação math.pow(base, expoente)
raiz mesmo processo.
'''
#Realizando operações básicas
numero1 = int(10)
numero2 = int(5)
numero3 = 16
#fazendo uma soma
soma = int(numero1 + numero2)
print(f'A soma de {numero1} + {numero2} = {soma}')
#fazendo subtração
subtracao = int(numero1 - numero2)
print(f'A subtração de {numero1} - {numero2} = {subtracao}')
# fazendo a divisao
divisao = float(numero1 / numero2)
print(f'A divisao de {numero1} / {numero2} = {divisao:.2f}')
# fazendo a multiplicacao
multiplicacao = int(numero1 * numero2)
print(f'A multiplicacao de {numero1} * {numero2} = {multiplicacao}')
# fazendo a precedencia
precedencia = float(numero1 * numero2 / numero1-numero1)
print(f'A precedencia de {numero1} por {numero2} = {precedencia:.2f}')
# por que deu esse resultado?
# fazendo a exponenciacao
exponenciacao = pow(numero1,2)
print(f'A exponenciacao de {numero1}² = {exponenciacao}')
# fazendo a raiz basta elevar a base por 0.5 ou 1/2 que dá a raiz quadrática
raiz = pow(numero3,1/2)
# fazendo a raiz cúbica
raiz1 = pow(numero3,1/3)
print(f'A raiz de {numero3} = {raiz1}')
# fazendo a resto da divisao
resto = int(numero1%2)
resto1 = int(numero1%3)
#10/2 qual sera o resto, deverá se o numero 0  \n->pula a linha
print(f'A resto de {numero1} % 2 = {resto}\n'
      f'E o resto de {numero1} % 3 = {resto1}')
# fazendo o quociente
quociente = int(numero1 // numero2)
print(f'A quociente de {numero1} // {numero2} = {quociente}')



