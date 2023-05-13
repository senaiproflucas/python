'''
Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares
Se o valor digitado for ímpar, desconsidere-o.'''

n = int(input('Digite a quantidade de vezes números pares se quer somar: '))
r = 0
for i in range(0, n):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        r += num
print(f"A soma dos pares:  {r}.")