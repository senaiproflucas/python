''' Prof. Luiz Henrique
Faça um programa que leia o sexo de uma pessoa
mas que deixe estrito apenas o sexo "M" ou "F".
O programa só liberará quando o usuário digitar
os valores.
Nota é muito importante negar a condição para deixá-la
estrita,o usuário digitará por infinitas vezes até
acertar. Para aplicativos via console é uma condição
muito interessante e muito utilizada. Pode ser feita
com palavras específicas, validar números etc.
'''

sexo = str(input("Digite M ou F: \n")).strip().upper()[0]
while sexo not in "MF": #em quanto o termo não estiver dentro de: ele não deixa por outros valores
    sexo = str(input("Digite apenas [M/F]: \n")).strip().upper()[0]
print("Sexo {} foi registrado com sucesso.".format(sexo))