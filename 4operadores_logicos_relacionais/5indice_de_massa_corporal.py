#faça um programa que calcule o índice de massa corporal
'''
Menor que 18,5	Magreza
18,5 a 24,9	Normal
25 a 29,9	Sobrepeso
30 a 34,9	Obesidade grau I
35 a 39,9	Obesidade grau II
Maior que 40	Obesidade grau III
'''
peso = str(input('Peso: ')).replace(',','.')
peso = float(peso)
altura = str(input('Altura: ')).replace(',','.')
altura = float(altura)
imc = peso/(pow(altura,2))
print(f'IMC = {imc:.2f}')
if(imc < 18.5):
    print(f'Abaixo do peso, seu IMC é {imc:.2f}')
elif(imc >= 18.5 and imc <= 24.99):
    print(f'Peso normal, seu IMC é {imc:.2f}')
elif(imc >= 25 and imc <= 29.99):
    print(f'Está com sobrepeso e seu IMC é {imc:.2f}')
elif(imc >= 30 and imc <= 34.99):
    print(f'Está com Obesidade Grau I e seu IMC é {imc:.2f}')
elif(imc >= 35 and imc <= 39.99):
    print(f'Está com Obesidade Grau II e seu IMC é {imc:.2f}')
else:
    print(f'Está com Obesidade Grau III e seu IMC é {imc:.2f}')
