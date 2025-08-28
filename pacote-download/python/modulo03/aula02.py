num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
num.insert(2,0)
print(num)
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
a = [2, 3, 4, 7]
b = a
b[2] = 8
c = a[:]

# EXERCICIO 78

lista = list()
for i in range (0, 5):
    A = int(input())
    lista.append(A)
    if i != 0:
        if lista[i] < menor:
            menor = lista[i]
            posicao_menor = i
        if lista[i] > maior:
            maior = lista[i]
            posicao_maior = i
    else:
        menor = lista[i]
        posicao_menor = i
        maior = lista[i]
        posicao_maior = i
print('Menor valor: {0}\nPosicao: {1}.'.format(menor, posicao_menor))
print('Maior valor: {0}\nPosicao: {1}.'.format(maior, posicao_maior))

# EXERCICIO 79

lista = list()
while True:
    num = int(input('Insira um número:'))
    if num in lista:
        continue
    else:
        lista.append(num)
    opcao = str(input('Deseja inserir mais números? [S/N]'))
    if opcao == 'N':
        break
lista.sort()
print(lista)

# EXERCICIO 80
maior = True
lista = list()
for i in range (0, 5):
    A = int(input('Insira um número:'))
    if i == 0 or A > lista[-1]:
        lista.append(A)
    else:
        pos = 0
        while pos < len(lista):
            if A <= lista[pos]:
                lista.insert(pos, A)
                break
            pos+=1
print(lista)

# EXERCICIO 81
lista = list()
while True:
    num = int(input('Insira um número:'))
    if num in lista:
        continue
    else:
        lista.append(num)
    opcao = str(input('Deseja inserir mais números? [S/N]'))
    if opcao == 'N':
        break
lista.sort(reverse=True)
if 5 in lista:
    foi = 'está'
else:
    foi = 'não está'
print(f'a) Foram digitados {len(lista)} números.\nb) {lista}\nc) O número 5 {foi} na lista.')

# EXERCICIO 82
lista = list()
pares = list()
impares = list()
while True:
    num = int(input('Insira um número:'))
    if num in lista:
        continue
    else:
        lista.append(num)
    opcao = str(input('Deseja inserir mais números? [S/N]'))
    if opcao == 'N':
        break
for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print(lista)
print(pares)
print(impares)

# EXERCICIO 83

abre = fecha = 0
primeiro = str(input('Insira a sua expressão: '))
separado = " ".join(primeiro)
expressao = separado.split()
for i in expressao:
    if i == '(':
        abre+=1
    if i == ')':
        fecha+=1
if abre == fecha:
    print('Sua expressão está correta.')
else:
    print('Sua expressão está errada.')
