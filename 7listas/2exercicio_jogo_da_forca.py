secreto = 'BORBOLETA'
digitado = []
chance = 3
while True:
    if chance <= 0:
        print('Você perdeu!!!')
    letra = input('Digite uma letra: ')
    #checagem
    if len(letra) > 1:
        print(f'Isso não vale, digite uma letra')
        continue
    digitado.append(letra)
    if letra in secreto :
        print(f'Parabéns a letra "{letra}" existe na palavra UHUUU')
    else:
        print(f'A letra "{letra}" não faz parte! Não foi dessa vez ')

    secretoTemporario = ''
    for letraSecreta in secreto :
        if letraSecreta in digitado :
            secretoTemporario += letraSecreta
        else:
            secretoTemporario += '*'
    if secretoTemporario == secreto:
        print(f'Que legal você ganhou!! a palavre é {secretoTemporario}')
    else:
        print(f'A palavra secreta está assim: {secretoTemporario}')
    if letra not in secreto:
        chance -= 1
        print(f'Você ainda tem {chance} chances')
        if chance == 0:
         print('Game Over')
         break
