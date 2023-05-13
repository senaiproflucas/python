'''Prof. Luiz Henrique
Variável Sinalizadora: “FLAG”
Um conceito/técnica interessante usado nas linguagens de programação é o emprego de
uma variável para sinalizar algum tipo de evento, situação ou estado do programa. Esta variável que
exerce a função de sinalizar alguma coisa é denominada de FLAG (“bandeira” em inglês).
Em muitas situações, o uso de flags pode simplificar bastante um programa. Podemos
trabalhar com flags que são variáveis booleanas (verdadeiro/falso) ou mesmo podemos usar uma
variável corrente do programa e através da atribuição de um valor especial para esta variável usá-la
para sinalizar alguma situação.
Exemplos de uso de Flags:
Crie um programa que leia vários números inteiros pelo teclado
O programa só vai parar quando o usuário digitar o valor 666,
que é a condição de parada

No final, mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag!)
'''

flag = False
contA = 0
contB = 0

while flag == False:
    num = int(input("Digite um número [666 para parar]: \n"))
    if num == 666:
        flag = True
    else:
        contA += num
        contB += 1
print("A soma é : {}.".format(contA))
print("Números digitados: {}.".format(contB))