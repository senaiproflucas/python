'''

Você com certeza já ouviu dizer que E = mc², onde E representa a energia (em Joules), m representa a massa (em quilogramas) e c representa a velocidade da luz (aproximadamente 300.000.000 m/s), essa fórmula foi descoberta por Albert Einstein e significa, em resumo, que massa e energia são equivalentes.

Crie um arquivo chamado einstein.py e escreva um programa em Python que use a massa indicada pelo usuário para calcular o valor equivalente em Joules de energia. Utilizar números inteiros e considerar que o usuário somente irá digitar números válidos.

Fique à vontade para utilizar as funções existentes do Python no link anexo da biblioteca, se precisar.

Exemplo:

Entrada:
m: 1
Saída:
E: 90000000000000000

Bônus:

Imprimir o resultado com o separador de milhar, exemplo:
E: 90,000,000,000,000,000

Bônus 2:

Trocar o separador de milhar de vírgula ( , ) para ponto ( . ), exemplo:
E:  90.000.000.000.000.000

'''

m = int(input("Digite a massa: "))
c = 300000000
E = m * c * c
#E = m * c ** 2
#E = m * pow(c,2)
E = '{:,}'.format(E).replace(',','.')
print("E: ",E)
#print("{i:,}").replace(",",".")