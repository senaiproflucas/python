''' Prof. Luiz Henrique
Crie um programa que leia uma frase qualquer
E diga se ela é um palíndromo, desconsiderando os espaços'''
# Socorram me subi no onibus em Marrocos
# Após a sopa
# A sacada da casa
# A torre da derrota
# o lobo ama o bolo
# Anotaram a data da maratona


palindromo = str(input("Digite a frase palíndroma: \n")).upper()
palindromo = "".join(palindromo.split(" "))
print("A palavra {} ao contrário é {} e ".format(palindromo, palindromo[::-1]), end="")
if palindromo == palindromo[::-1]:
    print("é um palíndromo.".format(palindromo))
else:
    print("não é um palíndromo.".format(palindromo))