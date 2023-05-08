'''
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
'''while(a<10):
    print(a)'''
#neste algoritmo o loop nao se quebra porque a vale 0 eternamente, depois dessa pegadinha vamos atribuir a
#atribuição +1
while (a<10):
    a+=1
    print(a)
