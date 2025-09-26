# EXERCICIO 96
def area(largura, comprimento):
    print(f"A área é de {largura * comprimento}m quadrados.")
largura = int(input('Insira a largura do tereno:'))
comprimento = int(input('Insira o comprimento do tereno:'))
area(largura, comprimento)

# EXERCICIO 97
def escreva(mensagem):
    print("-" * len(mensagem))
    print(mensagem)
    print("-" * len(mensagem))
escreva("Curso de Python no Youtube")

# EXECICIO 98
def contador(inicio, fim, passo):
    for i in range(1, 11):
        print(i, end=' ')
    print('FIM')
    for i in range(10, -1, -2):
        print(i, end=' ')
    print('FIM')
    for i in range(inicio, fim, passo):
        print(i, end=' ')
    print('FIM')
contador(0, 10, 1)

# EXERCICIO 99
def maior(* num):
    cont = maior = 0
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont+=1
    print(f'\nForam informados {cont} valores, o maior é {maior}.')
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(6)
maior()

# EXERCICIO 100
import random

numeros = list()
soma = 0
def sorteia():
    for i in range(0, 5):
        numeros[i] = random.randint(0, 10)
    somaPar()

def somaPar():
    for i in numeros:
        if i % 2 == 0:
            soma+=i
    print(f'A soma dos pares é {soma}.')
sorteia()


