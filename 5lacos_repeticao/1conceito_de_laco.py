'''
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
O melhor amigo de um laço são os acumuladores, uma variável pode acumular o valor dela + 1. Toda a
variável para ir para o laço tem que ser iniciada com um valor, geralmente iniciamos com 0 se for
string iniciamos com "" que significa vazio.
Laços de repetição são como engrenagens que ficam girando e movimentando o aparelho, imaginem uma
engrenagem com 10 dentes e quando seu dente chegar ao fim ela para ou assume outra função, uma engrenagem
de 10 dentes pode estar conectada com uma outra menor de 100 dentes e é isso que faz o movimento acontecer.
Os laços de repetição podem automatizar muitas tarefas e facilitar o processo.
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

