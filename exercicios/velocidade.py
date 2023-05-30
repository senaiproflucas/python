'''

Tem gente que fala rápido demais, mal dá pra entender, seria bom se a gente pudesse diminuir a velocidade ou até colocar umas pausas entre as palavras...

Crie um arquivo chamado velocidade.py e escreva um programa em Python que mostre uma mensagem digitada pelo usuário, mas substituindo os espaços em branco por reticências "...". 

Exemplo:

Mensagem: Não vejo a hora de ir embora
Saída: Não...vejo...a...hora..de...ir...embora

Bônus:

Retirar excessos de espaços antes de transformar nas reticências

'''

mensagem = input("Fale rápido: ")
print(mensagem.replace(" ", "..."))
print(" ".join(mensagem.split()).replace(" ", "..."))