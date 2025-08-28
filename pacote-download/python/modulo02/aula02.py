for c in range(1,6):
    print('Oi')
print('FIM')

for c in range(1,6):
    print(c)
print('FIM')

for c in range(6, 0, -1):
    print(c)
print('FIM')

for c in range(0, 7, 2):
    print(c)
print('FIM')

n = int(input('Insira um número:'))
for c in range(0, n):
    print(c)
print('FIM')

inicio = int(input('Insira um número:'))
fim = int(input('Insira um número:'))
passo = int(input('Insira um número:'))
for c in range(inicio, fim+1, passo):
    print(c)
print('FIM')

for c in range(0, 3):
    n = int(input('Insira um número:'))
print('FIM')

soma = 0
for c in range(0, 4):
    n = int(input('Insira um número:'))
    soma+=n
print('O somatório foi: {0}'.format(soma))

# EXERCICIO 46
import time

for n in range(10, -1, -1):
    print(n)
    time.sleep(1)

# EXERCICIO 47
for i in range(2, 51, 2):
    print(i)

# EXERCICIO 48
soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma+= i
print("A soma é {0}".format(soma))

# EXERCICIO 49
n = int(input('Insira um número:'))
for i in range (0, 11):
    print('{0} x {1} = {2}'.format(n, i, n * i))

# EXERCICIO 50
soma = 0
cont = 0
for i in range(0, 6):
    n = int(input('Insira um número: '))
    if n % 2 == 0:
        soma+= n
        cont+=1
print('Você me informou {0} números pares e a soma é {1}.'.format(cont, soma))

# EXERCICIO 51
termo = int(input('Insira o primeiro termo:'))
razao = int(input('Insira a razão:'))
print(termo)
for i in range (1, 10):
    print(termo + razao)
    termo = termo + razao

# EXERCICIO 52
primo = 0
n = int(input('Insira o número:'))
for i in range(n-1, 1, -1):
    if n % i == 0:
        print('Não é primo.')
        primo = 1
        break
if primo == 0:
    print('É primo')

# EXERCICIO 53
frase = str(input('Insira a frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):  
    inverso+= junto[letra]
if inverso == junto:
    print('É palíndromo.')
else:
    print("Não é palíndromo.")

# EXERCICIO 54
maior = 0
menor = 0
for i in range (0, 7):
    idade = int(input('Insira a sua idade:'))
    if idade >= 18:
        maior+= 1
    else:
        menor+= 1
print('Há {0} maiores de idade e {1} menores de idade.'.format(maior, menor))

# EXERCICIO 55
menor = float(input('Insira o peso:'))
maior = menor
for i in range (0, 5):
    atual = float(input('Insira o peso:'))
    if atual < menor:
        menor = atual
    elif atual > menor:
        maior = atual
print('O maior peso é {0} e o menor peso é {1}.'.format(maior, menor))

# EXERCICIO 56
media = 0
mulheres = 0
nome = str(input('Insira o nome:'))
idade = int(input('Insira a idade:'))
sexo = str(input('Insira o sexo:'))
if sexo == 'f':
        if idade < 20:
            mulheres+=1
            print('mais uma')
velho = idade
nome_mais = nome
media+=idade
for i in range (0,3):
    nome = str(input('Insira o nome:'))
    idade = int(input('Insira a idade:'))
    sexo = str(input('Insira o sexo:'))
    if sexo == 'f':
        if idade < 20:
            mulheres+=1
            print('mais uma')
    media+=idade
    elif sexo == 'm':
            if idade > velho:
                velho = idade
                nome_mais = nome
media = media / 4
print('A média de idades é {0} anos. O nome do homem mais velho é {1}. Há {2} mulher(es) com menos de 20 anos.'.format(media, nome_mais, mulheres))