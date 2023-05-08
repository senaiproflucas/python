'''
Jo Ken Po Elaborar um programa de jo ken po o usuário deverá escolher pedra papel e tesoura em um menu
e jogar contra o computador, para isso o computado deverá sortear de forma aleatória e o programa deverá
dizer quem ganhou a partida.
Para esta atividade é necessário conhcer o método random.randrange e o método time sleep
'''
from random import randrange
from time import sleep

print(40*'#')
print('JO-KEN-PO')
player = int(input('Olá bem vindo ao jogo do JO-Ken-PO\n'
              'Digite os números para a escolha\n'
              '1-Pedra\n'
              '2-Papel\n'
              '3-Tesoura\n'
              'Escolha: '))
if(player == 1):
    player = 'pedra'
elif(player ==2):
    player = 'papel'
elif(player ==3):
    player = 'tesoura'
else:
    print('Digite uma opção válida')
    exit()
computer = randrange(1,4)#sempre escolha um número acima
if(computer == 1):
    computer = 'pedra'
elif(computer ==2):
    computer = 'papel'
else:
    computer = 'tesoura'

sleep(1)
print('Jo', end = '-')#end deixa na mesma linha
sleep(1)
print('Ken', end = '-')
sleep(1)
print('Po')
if(player == computer):
    print(f'Empate player Jogou {player} e computador jogou {computer}')
elif(player == 'pedra' and computer == 'tesoura' or player == 'papel' and computer == 'pedra' or player == 'tesoura' and computer == 'papel'):
    print(f'Parabéns você ganhou! Player jogou {player} e computador jogou {computer}')
else:
    print(f'Que pena o computador superou! computador jogou {computer} e player jogou {player}')
print(40*'#')