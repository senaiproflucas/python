'''
QUANDO ESCREVE TUDO EM CAPS PARECE QUE A GENTE TÁ GRITANDO

Às vezes, precisamos ouvir nossa voz interior, e escrever tudo minúsculo para manter a paz.

Crie um arquivo chamado vozinterior.py e escreva um programa Python que pede ao usuário que digite uma frase, receba a frase e a retorne com todas as letras minúsculas. A pontuação, números e espaços em branco devem ser mantidos como digitado.

Lembre-se de testar o programa! Para rodar, acesse via terminal ou cmd o diretório onde ele está e use o comando: python vozinterior.py

Exemplo:
Entrada: AAAAAAAAH EU TÔ MALUCO
Saída: aaaaaaaah eu tô maluco

Bônus:

Além de deixar todas as letras minúsculas, imprima quantos caracteres a frase contém

'''

mensagem = input("Grite aqui: ")
print(mensagem.lower(), len(mensagem))