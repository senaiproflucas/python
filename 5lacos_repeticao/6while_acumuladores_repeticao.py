'''Prof. Luiz Henrique
while else
contadores/acumuladores
não é ideal fazer isso com o while, para isso usamos o for!
É apenas uma das formas de se utilizar o while, para verificar
as possibilidades do laço.
O While é mais indicado para repetições que não necessitam de
contagens exatas.
'''
contador = 1
acumulador = 1
while contador <= 10:
    print(contador,acumulador)
    acumulador = contador + acumulador
    contador += 1
    if contador > 5:
        break
else:#no comando while também aceita o else
    print('Cheguei no Else')