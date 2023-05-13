'''Prof. Luiz Henrique
Faça um programa que calcule a soma entre todos os números impares
que são múltiplos de três (3) e que se encontram no intervalo de 1 até 500.
Para isso é necessário utilizar um aninhamento de if
Chamamos de estruturas de decisão encadeadas, quando uma estrutura de decisão está
localizada dentro do lado falso da outra. Este tipo de estrutura também é conhecida
como seleção “aninhada” ou seleção “encaixada”.
Qualquer que seja o termo usado para identificar a estrutura, o importante é que esse
formato com uma estrutura de seleção dentro da outra permite fazer a escolha de apenas um
entre vários comandos possíveis.
'''

contSoma = 0  # Contador de soma
for num in range(1, 501):  # de 1 até 500
    if num % 2 != 0:  # Ímpares neste caso se faz um aninahmento de if um if dentro do outro
        if num % 3 == 0:  # Ímpares múltiplos de 3
            contSoma += num  # soma = soma + num
print(f"A soma dos múltiplos de 3 são: {contSoma}.")