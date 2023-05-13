''' Prof. Luiz Henrique
Faça um programa que leia um número inteiro e diga se ele é ou não
um número primo
nota para isso usaremos o operador floor //
// Floor Division - A divisão de operandos onde o resultado é o quociente
em que são retirados os dígitos após a vírgula. Mas se um dos operandos
for negativo, o resultado é nivelado, ou seja, arredondado a partir de zero
'''

num = int(input("Descubra se um número é primo: \n"))

primo = True
acm = (num // 2)#esta opção retorna o valor do quociente

for i in range(acm, 0, -1):
    if num % i == 0 and i != 1:
        primo = False

if primo:
    print("O número {} é primo.".format(num))
else:
    print("O número {} não é primo.".format(num))