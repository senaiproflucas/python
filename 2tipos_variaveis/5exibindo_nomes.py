print("Exercício")
'''
* Criar Variáveis para nome (str), idade (int),
* altura float e peso float de uma pessoa
* Obter o ano de nascimento da pessoa (baseado na idade e ano)
*atual
* Obter IMC da pessoa com duas casas decimais
* Exibir um texto com todos os valores na tela usando F-Strings
*Com as chaves
'''
#Solução
import math
nome = "gabriel"
idade = 25
anoAtual = 2021
anoNasc = anoAtual - idade
peso = 89.0
altura = 1.82
imc = (peso/(pow(altura, 2)))

print(f"{nome}, {idade}, {peso}, {altura}, {anoNasc}, {imc:.2f}")
print("nome e sobrenome")