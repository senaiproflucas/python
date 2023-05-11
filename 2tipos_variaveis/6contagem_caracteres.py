'''
Função len
permite a contagem dos caracteres, ótimo para limitar numero de
caracteres.
'''
usuario = input('Digite o usuário: ')
qtCaracteres = len(usuario)
if qtCaracteres <6:
    print(f'É necessário digitar pelo menos 6 caracteres')
else:
    print(f'Você foi cadastrado no sistema')
string1 = input('Digite algo: ')
string2 = input('Digite algo a mais: ')
print(f'A soma dos caracteres é: {len(string1) + len(string2)} ')
print (string2.__len__()) # string2.chama o metodo __len__
'''
Cada função que se invóca por trás tem um método.
Em python também pode construir métodos e chamá-lo
Veremos mais adiante em orientaçãoa bojetos POO
'''


