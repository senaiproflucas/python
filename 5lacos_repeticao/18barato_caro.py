'''Prof. Luiz Henrique
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a) qual é o total gasto na compra
b) quantos produtos custam mais de R$ 1000
c) qual é o nome do produto mais barato
'''
nomeProduto = ""
resultado = maior = menor = 0

while True:
    name = str(input("Digite o nome do produto: \n"))
    preco = float(str(input("Preço: \n")).replace(',','.').strip())

    resultado += preco

    if preco > 1000:
        maior += 1

    if menor == 0:
        menor = preco
        nomeProduto = name
    elif preco < menor:
        menor = preco
        nomeProduto = name

    sair = str(input("Inserir mais produtos? [S / N] \n")).strip().upper()[0]
    while sair not in 'NS':
        sair = str(input("Inserir mais produtos? [S / N] \n")).strip().upper()[0]

        if sair == 'S' or sair == 'N':
            break
        else:
            print('Digite apenas [S/N]')

    if sair == "N":
        print(f"Total gasto: R${resultado:.2f}")
        print(f"Produtos que custam mais do que R$1.000: {maior}")
        print(f"O produto mais barato é {nomeProduto}, que custa R${menor:.2f}")
        break