n = (input('Insira um número: '))
print(n)
print(type(n))
print(n.isnumeric())
print(n.isnumeric()) # se é letra

# DESAFIO 4

variavel = input('Digite algo: ')
print('O tipo é {}'.format(type(variavel)))
#print('O tipo é ', type(variavel))
print('É número? {}'.format(variavel.isnumeric()))
#print('É número? ', variavel.isnumeric())
print('Só tem espaço? {}'.format(variavel.isspace()))
#print('Só tem espaço? ', variavel.isspace())
print('É alfabético? {}'.format(variavel.isalpha()))
#print('É alfabético? ', variavel.isalpha())
print('É alfanumérico? {}'.format(variavel.isalnum()))
#print('É alfanumérico? ', variavel.isalnum())
print('Está em maiúsculas? {}'.format(variavel.isupper()))
#print('Está em maiúsculas? ', variavel.isupper())
print('Está em minúsculas? {}'.format(variavel.islower()))
#print('Está em minúsculas? ', variavel.islower())
print('Está capitalizado? {}'.format(variavel.istitle()))
#print('Está capitalizado? ', variavel.istitle())

