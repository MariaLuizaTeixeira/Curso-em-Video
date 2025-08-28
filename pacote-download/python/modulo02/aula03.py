for c in range(1, 10):
    print(c)
print('Fim')

c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')

for c in range(1, 3):
    n = int(input('Insira um valor: '))
print('Fim')

c= 1
while c != 0:
    c = int(input('Insira um valor: '))
print('Fim')

r = 'S'
while r != 'S':
    c = int(input('Insira um valor: '))
    c = str(input('Deseja continuar [S/N]: ')).upper()
print('Fim')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor:'))
    if n % 2 == 0:
        par += 1
    else: 
        impar += 1
        print('impar')
        print(impar)
print('Bocê digitou {0} pares e {1} ímpares!'.format(par - 1, impar))

# EXERCICIO 57
opcao = str(input('Insira a opção: ')).strip

while opcao not in 'MmFf':
    opcao = input('Dados inválidos. Insira a opcao: ').strip

# EXERCICIO 58
import random
computador = random.randint(0, 10)
chute = 99
palpite = 0
while chute != computador:
    chute = int(input('Insira o seu chute:'))
    palpite +=1
print('Você acertou! Foram necessários {0} palpites para acertar.'.format(palpite))

# EXERCICIO 59
opcao = 0
v1 = int(input('Insira o valor 1: '))
v2 = int(input('Insira o valor 2: '))

while opcao != 5:
    print('---------- MENU ----------')
    print('[1] - SOMAR')
    print('[2] - MULTIPLICAR')
    print('[3] - MAIOR')
    print('[4] - NOVOS NÚMEROS')
    print('[5] - SAIR DO PROGRAMA')

    opcao = int(input('Insira a sua opção: '))

    if opcao == 1:
        soma = v1 + v2
        print('A soma é {0}'.format(soma))
    elif opcao == 2:
        produto = v1 * v2
        print('O produto é {0}'.format(produto))
    elif opcao == 3:
        if v1 > v2: 
            maior = v1
            print('O maior é {0}'.format(maior))
        elif v2 > v1: 
            maior = v2
            print('O maior é {0}'.format(maior))
        else : 
            print('Eles são iguais.')
    elif opcao == 4:
        v1 = int(input('Insira o valor 1: '))
        v2 = int(input('Insira o valor 2: '))
print('Programa encerrado.')

# EXERCICIO 60
fatorial = 1
numero = int(input('Insira o seu número: '))
while numero != 1:
    fatorial = fatorial * numero
    numero-= 1
print('O fatorial é: {0}.'.format(fatorial))

# EXERCICIO 61

razao = int(input('Insira a razão:'))
termo = int(input('Insira o termo:'))
i = 0
while i != razao:
    termo = termo + razao
    print(termo)
    i+=1

# EXERCICIO 62

razao = int(input('Insira a razão:'))
termo = int(input('Insira o termo inicial:'))
cont = int(input('Insira a quantidade de termos: '))
while cont != 0:
    termo = termo + razao
    print(termo)
    cont-=1
    if cont == 0:
        cont = int(input('Insira a quantidade de termos: '))

# EXERCICIO 63
n = int(input('Insira um número:'))
antigo = 0
atual = 1
intermediario = atual
print(antigo)
print(atual)
while n - 2 != 0:
    atual += antigo
    antigo = intermediario
    intermediario = atual
    print(atual)
    n-=1

# EXERCICIO 64
soma = n = cont = 0
while n != 999:
    n = int(input('Insira um número: '))
    soma +=n
    cont+=1
print('Você digitou {0} números e a soma foi {1}.'.format(cont - 1, soma - 999))

# EXERCICIO 65
media = cont = 0
n = int(input('Insir um número:'))
cont+=1
media +=n 
menor = maior = n 
continuar = 's'
while continuar == 's':
    n = int(input('Insira um número: '))
    cont+=1
    media +=n
    if maior > n:
        menor = n 
    else:
        maior = n 
    continuar = input('Deseja continuar? [s/n]')
media = media / cont
print('A média foi {0}, o menor número foi {1} e o maior foi {2}.'.format(media, menor, maior))
