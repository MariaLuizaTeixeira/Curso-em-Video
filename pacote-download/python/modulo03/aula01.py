lanche = ('Hambúrguer', 'Suco', 'Pudim', 'Pizza')
print(lanche)
print(lanche[3])
print(lanche[-1])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-3:]) 
print(len(lanche))
for comida in lanche:
    print(f'Eu vou comer {comida}.')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}.')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}.')
print(sorted(lanche))
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b 
print(c)
print(c.count(5))
print(c.index(8))
del(c)

# EXERCICIO 72

numeros = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte']
n = int(input('Insira o número que deseja ler: '))
while True:
    if n >= 0 and n <= 20:
        break
    else: 
        n = int(input('Digite novamente: '))
print(f'Você digitou o número {numeros[n]}.')

# EXERCICIO 73

times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Bahia', 'Botafogo', 'Mirassol', 'São Paulo', 'Fluminense', 'Bragantino', 'Ceará SC', 'Atlético-MG', 'Internacional', 'Grêmio', 'Corinthias', 'Santos', 'Vasco da Gama', 'EC Vitória', 'Juventude', 'Fortaleza', 'Sport Recife')
print(f'a) Primeiros seis colocados: {times[0:5]}.')
print(f'b) Quatro últimos colocados: {times[-4:]}.')
print(f'c) Em ordem alfabética: {sorted(times)}.')
if 'Chapecoense' in times:
    print(f'd) Chapecoense na posição {times.index('Chapecoense') + 1}.')
else:
    print('A Chapecoense não se encontra na série A.')

# EXERCICIO 74

from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram ', end="")
for i in numeros:
    print(i, end=" ")
menor = maior = numeros[0]
for i in range (0, len(numeros)):
    if numeros[i] < menor:
        menor = numeros[i]
for i in range (0, len(numeros)):
    if numeros[i] > maior:
        maior = numeros[i]
print(f'\nO maior valor foi {maior}.\nO menor valor foi {menor}.')

from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram ', end="")
for i in numeros:
    print(i, end=" ")
print(f'\nO maior valor foi {max(numeros)}.\nO menor valor foi {min(numeros)}.')

# EXERCICIO 75

pares = nenhum = 0
v1 = int(input('Insira um número:'))
v2 = int(input('Insira um número:'))
v3 = int(input('Insira um número:'))
v4 = int(input('Insira um número:'))
numeros = (v1, v2, v3, v4)
print(f'O número 9 apareceu {numeros.count(9)} vez(es).')
if 3 in numeros:
    print(f'O número 3 apareceu na {numeros.index(3)}ª posição.')
else:
    print('O número 3 não foi digitado.')
print('Os números pare digitados foram:')
for i in numeros:
    if i % 2 == 0:
        print(i, end=" ")
    else:
        nenhum+=1
if nenhum == 4:
    print('Nenhum.')

# EXERCICIO 76
tupla = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.35, 'Canetas', 22.30, 'Livro', 34.90)
cont = 0
while True:
    if cont <= len(tupla) - 1:
        print(f'{tupla[cont]} -> {tupla[cont + 1]}')
        cont+=2
    else:
        break

# EXERCICIO 77
tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR')
for i in tupla:
    print(f'Na palavra {i} temos as vogais ', end="")
    for j in ' '.join(i):
        if j in 'AEIOU':
            print(j, end=" ")
    print('\n')



