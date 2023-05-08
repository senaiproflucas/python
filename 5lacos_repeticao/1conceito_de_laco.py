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
a = 0
a = a + 1 # qual será o valor da variável a?
print(a)
a += 1 #é outra forma de escrever a mesma coisa se coloca o sinal de soma na frente e adiciona 1
print(a)
#agora imaginem ter que fazer esse acumulador chegar a 10, 100 ou a 1000. Perderia muito tempo digitando linha à linha
#nesse sentido o python ajuda no processo de automação. Veja que coisa simples.
a = 0 #resetou a variável a agora ela vale 0
while(a<10):
    print(a)
#neste algoritmo o loop nao se quebra porque a vale 0 eternamente, depois dessa pegadinha vamos atribuir a
#atribuição +1

while (a<10):
    a+=1
    print(a)
