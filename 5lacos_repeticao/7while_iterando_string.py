''' prof. Luiz Henrique Trabalhando com índices
Indices
123456789 ...33'''
frase ='Quando a educação não é libertadora o oprimido quer tomar o lugar do opressor'
tamanhoFrase = len(frase)
contador = 0
fraseNova = ''
fraseNova1 = ''
# while contador < tamanhoFrase:
#     #print(frase[contador],contador)
#     fraseNova += frase[contador]
#     contador += 1
#     print(fraseNova)
    #faz checagem
while contador < tamanhoFrase:
    letra = frase[contador]
    if letra == 'r':
        fraseNova1 += 'R'
    else:
        fraseNova1 += letra
    contador += 1 #contador recebe contador = contador + 1
print(fraseNova1)