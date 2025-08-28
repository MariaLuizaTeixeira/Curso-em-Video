cont = 1
while cont<=10:
    print(cont, ' ', end ='')
    cont+=1
print('Acabou')

cont = 1
while True:
    print(cont, ' ', end ='')
    cont+=1
print('Acabou')

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s+=n
print(f'A soma é {s}')

# EXERCICIO 66

s = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s+=n
    cont+=1
print(f'Foram digitados {cont} números e a soma é {s}. ')

# EXERCICIO 67

while True:
    n = int(input('Insira um número: '))
    if n < 0:
        break
    else:
        for i in range (0, 10):
            print(f'{n} x {i} = {n * i}')
print('Programa encerrado!')

# EXERCICIO 68

from random import randint 
cont = 0
while True:
    opcao = int(input('[1] - Par\n[2] - Ímpar:'))
    numero_computador = randint(1, 10)
    print(numero_computador)
    if opcao == 1:
        numero_pessoa = int(input('Insira um número: '))
        if (numero_computador + numero_pessoa) % 2 == 0:
            print('Parabéns! Você ganhou')
            cont+=1
        else:
            break
    elif opcao == 2:
        numero_pessoa = int(input('Insira um número: '))
        if (numero_computador + numero_pessoa) % 2 == 0:
            break
        else:
            print('Parabéns! Você ganhou')
            cont+=1
    else:
        print('Opção inválida!')
print(f'Você perdeu dessa vez, mas ganhou {cont} jogos.')

# EXERCICIO 69

maior = homem = mulher = 0
while True:
    idade = int(input('Insira a sua idade:'))
    sexo = str(input('Insira o seu sexo: [H/M]'))
    if idade >= 18:
        maior+=1
    if sexo in 'Hh':
        homem+=1
    else:
        if idade < 20:
            mulher+=1
    continuar = int(input('[1] - Continuar\n[2] - Parar\n'))
    if continuar == 1:
        continue
    elif continuar == 2:
        break
    else:
        print('Opção inválida.')
print(f'Há {maior} pessoa(s) com mais de 18 anos, {homem} homem(ns) foram cadastrados e há {mulher} mulher(es) com menos de 20 anos.')

# EXERCICIO 70
total = mais1000 = 0
cont = 1
while True:
    nome = str(input('Insira o nome do produto: '))
    preco = float(input('Insira o preço do produto: '))
    total+=preco
    if preco > 1000:
        mais1000+=1
    if cont > 1:
        if preco < preco_barato:
            nome_barato = nome
    else:
        preco_barato = preco
        nome_barato = nome
    cont+=1
    continuar = int(input('[1] - Continuar\n[2] - Parar\n'))
    if continuar == 1:
        continue
    elif continuar == 2:
        break
    else:
        print('Opção inválida.')
print(f'O total é de R$ {total}. {mais1000} produto(s) custam mais de R$ 1000.00. O produto mais barato é {nome_barato}.')

# EXERCICIO 71

nota50 = nota20 = nota10 = nota1 = 0
print('----------CAIXA ELETRÔNICO ----------')
valor = int(input('Insira o valor a ser sacado:\nR$'))
while True:
    if valor == 0:
        break
    elif valor - 50 >= 0:
        valor = valor - 50
        nota50+=1
    elif valor - 20 >= 0:
        valor = valor - 20
        nota20+=1
    elif valor - 10 >= 0:
        valor = valor - 10
        nota10+=1
    else:
        valor = valor - 1
        nota1+=1
print(f'Serão necessárias:\n{nota50} notas de R$50,00.\n{nota20} notas de R$20,00.\n{nota10} notas de R$10,00.\n{nota1} notas de R$1,00.')
    