'''
For in Python
Iterando strings com for
Função range(start = 0, stop, step = 1
range não depende do for e nem o for depende dela, porém as
duas se dão muito bem juntos.
'''
texto = 'centriolo'
novaString = ''
for letra in texto:
    print(letra)
print('#############@@@@@@@@@@#########')
#start(número que inicia, stop(número que para, step(pula)
for n in range(10):
    print(n)
print('#############@@@@@@@@@@#########')

for n in range(0, 100, 8):
    print(n)
print('#############@@@@@@@@@@#########')
for n in range(100):
    if n % 8 == 0:
        print(n)
print('#############@@@@@@@@@@#########')

for letra in texto:
    if letra == 't':
        novaString += letra.upper()
    elif letra == 'o':
        novaString += letra.upper()
    else:
        novaString += letra
print(novaString)
#pode usar continue e o break
