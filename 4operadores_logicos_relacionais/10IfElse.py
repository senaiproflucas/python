'''Prof. Luiz henrique
Condições If Elif e Else
Executa comparações e a partir das comparações se tem um resultado

Fazer o teste de messa
if true:
    print('verdadeiro')
    Else:
    print(false)
Operadores Relacionais
menor <, menor/igual <=, maior >, maior/igual >=, diferente !=, igual ==
Condições Lógicas: AND, OR, NOT, IF
Na teoria dos conjuntos quando se tem um universo A e um universo B, há entre
esses conjuntos, a união, não união, intersecção, ou não intersecção. para que
se estabeleça soluções lógicas, é importante trabalhar com essas teorias e para
isso se usa o and, or, not, if.
Contudo há erros matemáticos que impedem o programa de rodar e ele trava, isso
não é bom para a experiência do usuário e para isso devemos tratar esses erros.
Uma das formas de tratar o erro e trabalhando com o try e o exception.
Ele nada mais faz do que dar uma mensagem caso ocorra um erro.
Exemplo vamos pedir para o python comparar dois valores e se o usuário digitar letras
ao invés de números
'''
try: #Não deixa o usuário digitar caractere
    num1 = int(input('digite o valor 1:  '))
    num2 = int(input('Digite o valor 2: '))
    if(num1 == num2):
        print(f'Os valores são Iguais {num1}')
    else:
        print(f'Possuem valores diferentes {num1} e {num2}')
except:
    print('ERROR')
#Obs: Pass e Elipsis serve para deixar a condição em branco e depois editar

nome = False
if nome == True:
    ... #pode usar o False
else:
    print('Opção Inválida')