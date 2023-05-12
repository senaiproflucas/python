'''
Elabore um programa que calcule o valor a ser pago de um produto,
leve em conta o preço normal mais a condição de pagamento:

- à vista dinheiro: 5% de desconto
- à vista no cartão: 10% de desconto
- em até 2vezes no cartão: preço normal
- em 3vezes ou mais no cartão: 13,5% de juros
'''
valor = float(input("Qual o preço do produto? \n"))
print("Selecione uma forma de pagamento")
print('''
Digite 1: Para pagar à vista no dinheiro.
Digite 2: Para pagar à vista no cartão.
Digite 3: Em 2x no cartão.
Digite 4: Em 3x no cartão ou mais \n''')
pagamento = int(input("Selecione a forma de pagamento: \n"))

if pagamento == 1:  # 5% de desconto
    print("Você selecionou à vista no dinheiro.")
    desconto = (valor * (5/100))
    print("Valor à vista no dinheiro: R${:.2f}.".format(
        valor - desconto)
    )
elif pagamento == 2:  # 10% de desconto
    print("Você selecionou à vista no cartão.")
    desconto = (valor * (10 / 100))
    print("Valor à vista no cartão: {:.2f}.".format(
        valor - desconto)
    )
elif pagamento == 3:  # Em até 2x no cartão: preço normal
    print("Você selecionou em 2x no cartão.")
    print("Pagamento em 2x de R${:.2f}.".format((valor / 2))
          )

elif pagamento == 4:  # Em até 3x ou mais: 13.5% de juros
    print("Você selecionou em 3x ou mais no cartão.")
    desconto = (valor * (13.5 / 100))
    parcelas = int(input("Em quantas vezes você deseja parcelar? \n"))
    if parcelas < 3:
        print("A quantidade mínima de parcelas é de 3x no cartão.")
    else:
        print("Pagamento, com juros de 13.5%, em {}x de R$ {:.2f}.".format(
            parcelas, (valor + (desconto)) / parcelas))
else:
    print("Selecione uma opção válida.")