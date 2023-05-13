'''Prof. Luiz Henrique
Existem dois tipos de laços de repetição o for e o while.
O laço for é ideal para contagens numéricas, sobre ele pode-se fazer sequências aritméiticas como
Progreção Aritmética (PA) e Progressão Geométrica (PG).
Podemos também calcular matriz, fazendo linha e coluna.
O for ele no python é tamos que levar em conta o range. O alcance, conforme o exemplo:
for i in range(0,10,1) -> esta condição indica a variável i; in - é que está dentro; range é o alcance
entre parenteses está incluído o valor que o i ira começar, 10 é até o número que será incrementado e o 1
é o numero de saltos que o for faz. Como por padrão pular de 1 em 1 já é uma função nativa então não precisa
informar o salto se for pular de 1 em 1.
for i in range(0,10) -> irá mostrar a sequência 12345678910 como saída.
O while é uma condição lógica. O laço de repetição nada mais é que enquanto a condição for verdadeira
o laço se perpetuara até que atinja o que foi definido à partir deste momento o algorítmo sai do laço
ele segue o fluxo que foi programado.
De muitas maneiras, o objeto retornado por range()se comporta como se fosse uma lista, mas na verdade não é.
É um objeto que retorna os itens sucessivos da sequência desejada quando você itera sobre ele, mas não faz
parte da lista, economizando espaço.

Dizemos que tal objeto é iterável , ou seja, adequado como alvo para funções e construções que esperam algo
do qual possam obter itens sucessivos até que o suprimento se esgote.
O melhor amigo de um laço são os acumuladores, uma variável pode acumular o valor dela + 1. Toda a
variável para ir para o laço tem que ser iniciada com um valor, geralmente iniciamos com 0 se for
string iniciamos com "" que significa vazio.
Laços de repetição são como engrenagens que ficam girando e movimentando o aparelho, imaginem uma
engrenagem com 10 dentes e quando seu dente chegar ao fim ela para ou assume outra função, uma engrenagem
de 10 dentes pode estar conectada com uma outra menor de 100 dentes e é isso que faz o movimento acontecer.
Os laços de repetição podem automatizar muitas tarefas e facilitar o processo.
A breakinstrução, como em C, sai do fechamento forou whileloop mais interno.

As instruções de loop podem ter uma elsecláusula; ele é executado quando o loop termina por exaustão do
iterável (com for) ou quando a condição se torna falsa (com while), mas não quando o loop é finalizado por
uma breakinstrução. Isso é exemplificado pelo seguinte loop, que procura por números primos:


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
(Sim, este é o código correto. Observe atentamente: a elsecláusula pertence ao forloop, não à ifinstrução.)

Quando usada com um loop, a elsecláusula tem mais em comum com a elsecláusula de uma tryinstrução do que com a das ifinstruções: a cláusula tryde uma instrução elseé executada quando nenhuma exceção ocorre e a elsecláusula de um loop é executada quando não break ocorre. Para saber mais sobre a tryinstrução e as exceções, consulte Manipulando exceções .

A continueinstrução, também emprestada de C, continua com a próxima iteração do loop:


for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9
'''


#exemplo de acumulador
i = 0
i = i + 1 # qual será o valor da variável a?
print(i)
i += 1 #é outra forma de escrever a mesma coisa se coloca o sinal de soma na frente e adiciona 1
print(i)
print('começando o for')
#agora imaginem ter que fazer esse acumulador chegar a 10, 100 ou a 1000. Perderia muito tempo digitando linha à linha
#nesse sentido o python ajuda no processo de automação. Veja que coisa simples.

#construindo o laço for
#automaticamente ele irá incrementar de 1 em 1.
#nota que no pyton ele sempre ira incrementar 1 e nunca o 0 se quiser que o for comece do 1 tem que inserir 1
for i in range(0,10):
    print(i)
print('Aplicando o salto 2')
#ele irá incrementar o número de saltos
for i in range(0,10,2):
    print(i)
#fazendo tudo ser impresso na mesma linha
for i in range(0,10):
    print(i, end = '->')
print('fim')
#começando do 0
for i in range(1,10):
    print(i, end = '->')
print('fim')
#neste caso há um problema vai até o 9 e não até o 10 se precisar que vá até o 10 deve inserir +1 ou 11 no range
for i in range(1,10+1):
    print(i, end = '->')
print('fim')
'''
Estrutura do for
o for ele precisa de um valor inical, que será definio no inicio for var in(percorrerá a var) range(valor inical de var, até onde vai var, salto)
em outras lingugens o for é um bloco 
for(i=0;i<10;i++){
    o for será executado aqui
}
No python existe essa sintaxe conforme trabalhada.
Agora é importante fazer um for com decrementando menos um
'''
#neste exemplo o valor de i começa com 10, o alcance até 0 e o salto -1, ou seja um decremento, mas não vai até 0
for i in range(10,0,-1):
    print(i, end = '->')
print('fim')
#fazendo um decremento até 0 contudo haverá 11 incrementos na contagem.
for i in range(10,-1,-1):
    print(i, end = ' ')#foi inserido um espaço aqui
print('fim')

