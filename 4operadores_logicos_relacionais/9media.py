'''Elaborar um programa em que o usuário digita 4 notas float com duas casas decimais e o sistema calcula a
média com duas casas decimais no final, importante fazer tratamento de variáveis'''
nota1 = float(str(input('Digite a nota 1: ').replace(',','.').strip()))#aqui o cast já foi realizado no início
nota2 = float(str(input('Digite a nota 2: ').replace(',','.').strip()))
nota3 = float(str(input('Digite a nota 3: ').replace(',','.').strip()))
nota4 = float(str(input('Digite a nota 4: ').replace(',','.').strip()))
if(nota1<0 and nota1>10 or nota2<0 and nota2>10 or nota3<0 and nota3>10 or nota4<0 and nota4>10):
    print('Digete notas entre 0 e 10')
else:
    #importante fazer um cast para converter string em float, contudo outra forma de fazer o cast é como está acima
    # nota1 = float(nota1)
    # nota2 = float(nota2)
    # nota3 = float(nota3)
    # nota4 = float(nota4)
    media = round((nota1+nota2+nota3+nota4)/4, 2)#método round() que arredonda números matemáticos
    print(f'A média é: {media}')
