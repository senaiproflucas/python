'''Prof. Luiz Henrique
fazer uma progressão arimética utilizando o for
A Progressão Aritmética (P.A.) é uma sequência de números onde a diferença entre dois termos consecutivos é
sempre a mesma. Essa diferença constante é chamada de razão da P.A..

Sendo assim, a partir do segundo elemento da sequência, os números que surgem são resultantes da soma da
constante com o valor do elemento anterior.

Isso é o que a diferencia da progressão geométrica (P.G.), pois nesta, os números são multiplicados pela razão,
enquanto na progressão aritmética, eles são somados.

As progressões aritméticas podem apresentar um número determinado de termos (P.A. finita) ou um número infinito
de termos (P.A. infinita).

Para indicar que uma sequência continua indefinidamente utilizamos reticências, por exemplo:

a sequência (4, 7, 10, 13, 16, ...) é uma P.A. infinita.
a sequência (70, 60, 50, 40, 30, 20, 10) é uma P.A. finita.
Cada termo de uma P.A. é identificado pela posição que ocupa na sequência e para representar cada termo utilizamos
uma letra (normalmente a letra a) seguida de um número que indica sua posição na sequência.

Por exemplo, o termo a4 na P.A (2, 4, 6, 8, 10) é o número 8, pois é o número que ocupa a 4ª posição na sequência.

Classificação de uma P.A.
De acordo com o valor da razão, as progressões aritméticas são classificadas em:

Constante: quando a razão for igual a zero. Por exemplo: (4, 4, 4, 4, 4...), sendo r = 0.
Crescente: quando a razão for maior que zero. Por exemplo: (2, 4, 6, 8,10...), sendo r = 2.
Decrescente: quando a razão for menor que zero (15, 10, 5, 0, - 5,...), sendo r = - 5
Propriedades da P.A.
1ª propriedade:
Em uma P.A. finita, a soma de dois termos equidistantes dos extremos é igual à soma dos extremos.

Exemplo
propriedades da pa

2ª propriedade:
Considerando três termos consecutivos de uma P.A., o termo do meio será igual a média aritmética
dos outros dois termos.

Exemplo
propriedades progressões aritiméticas

3ª propriedade:
Em uma P.A. finita com número de termos ímpar, o termo central será igual a média aritmética entre
termos equidistantes deste. Esta propriedade deriva da primeira.

propriedades progressão aritmética

Veja também: Média Aritmética
Fórmula do Termo Geral
começar estilo tamanho matemático 26px a com n subscrito igual a a com 1 subscrito mais parêntese esquerdo
n menos 1 parêntese direito. r fim do estilo

Onde,

an: termo que queremos calcular
a1: primeiro termo da P.A.
n: posição do termo que queremos descobrir
r: razão

Explicação da fórmula
Como a razão de uma P.A. é constante, podemos calcular seu valor a partir de quaisquer termos consecutivos, ou seja:

r igual a a com 2 subscrito menos a com 1 subscrito igual a a com 3 subscrito menos a com 2 subscrito
igual a a com 4 subscrito menos a com 3 subscrito igual a... igual a a com n subscrito menos a com n
menos 1 subscrito fim do subscrito

Sendo assim, podemos encontrar o valor do segundo termo da P.A. fazendo:

a com 2 subscrito menos a com 1 subscrito igual a r espaço espaço seta dupla para a direita espaço a com 2
subscrito igual a a com 1 subscrito mais r

Para encontrar o terceiro termo utilizaremos o mesmo cálculo:

a com 3 subscrito menos a com 2 subscrito igual a r espaço espaço seta dupla para a direita espaço a com
3 subscrito espaço igual a a com 2 subscrito mais r espaço

Substituindo o valor de a2, que encontramos anteriormente, temos:

a com 3 subscrito igual a parêntese esquerdo a com 1 subscrito mais r parêntese direito mais r a com 3
subscrito igual a a com 1 subscrito mais 2 r

Se seguirmos o mesmo raciocínio, podemos encontrar:

a com 4 subscrito menos a com 3 subscrito igual a r espaço espaço seta dupla para a direita espaço a com 4
subscrito espaço igual a a com 3 subscrito mais r espaço seta dupla para a direita a com 4 subscrito igual a a
com 1 subscrito mais 3 r

Observando os resultados encontrados, notamos que cada termo será igual a soma do primeiro termo com a razão
multiplicada pela posição anterior.

Esse cálculo é expresso através da fórmula do termo geral da P.A., que nos permite conhecer qualquer elemento
de uma progressão aritmética.

Exemplo
Calcule o 10° termo da P.A.: (26, 31, 36, 41, ...)

Solução

Primeiro, devemos identificar que:

a1 = 26
r = 31 - 26 = 5
n = 10 (10º termo).

Substituindo esses valores na fórmula do termo geral, temos:

an = a1 + (n - 1) . r
a10 = 26 + (10-1) . 5
a10 = 26 + 9 .5
a10 = 71

Portanto, o décimo termo da progressão aritmética indicada é igual a 71.

Fórmula do termo geral a partir de um termo k qualquer
Muitas vezes, para definir um termo genérico qualquer, que chamamos de an, não temos o primeiro termo a1,
mas conhecemos outro qualquer, que chamamos de ak.

Podemos usar a fórmula do termo geral a partir de um termo k qualquer:

começar estilo tamanho matemático 26px a com n subscrito igual a a com k subscrito mais parêntese esquerdo n
menos k parêntese direito. r fim do estilo

Repare que a única diferença, foi a mudança do índice 1 na primeira fórmula, pelo k, na segunda.

Sendo,

an: o n-ésimo termo da P.A. (um termo numa posição n qualquer)
ak: o k-ésimo termo de uma P.A. (um termo numa posição k qualquer)
r: a razão

Soma dos Termos de uma P.A.
Para encontrar a soma dos termos de uma P.A. finita, basta utilizar a fórmula:

começar estilo tamanho matemático 26px S com n subscrito igual a numerador parêntese esquerdo a com 1 subscrito
mais a com n subscrito parêntese direito. n sobre denominador 2 fim da fração fim do estilo

Onde,

Sn: soma dos n primeiros termos da P.A.
a1: primeiro termo da P.A.
an: ocupa a enésima posição na sequência (uma termo na posição n)
n: posição do termo

no algorítmo fica   t1  t2  t3
                        t1  t2  t3
                            t1  t2  t3


'''
#fazer uma programa que o cliente digita o termo inical e há a contagem de 10 termos com salto de 2
n = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
t1 = n
for i in range(0, 10):
    t1 += razao
    print(t1, end=' ')