# Indices
# 123456789 ...33
frase ='O rato roeu a roupa do rei de roma'
tamanhoFrase = len(frase)
contador = 0
novaString = ''
novaString1 = ''
# while contador < tamanhoFrase:
#     #print(frase[contador],contador)
#     novaString += frase[contador]
#     contador += 1
#     print(novaString)
    #faz checagem
while contador < tamanhoFrase:
    letra = frase[contador]
    if letra == 'r':
        novaString1 += 'R'
    else:
        novaString1 += letra
    contador += 1
print(novaString1)