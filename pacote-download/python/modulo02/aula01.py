nome = str(input('Qual é o seu nome?\n'))
if nome == 'Gustavo':
    print('Que nome lindo!')
elif nome == 'Malu':
    print('Que nome maravilhoso!')
else:
    print('Que nome feio!')

# EXERCICIO 36

casa = float(input('Insira o valor da casa:\n'))
salario = float(input('Insira o salário:\n'))
anos = int(input('Insira em quantos anos você vai pagar a casa:'))

meses = anos * 12
prestacao = casa / meses
if prestacao > (salario * 30) / 100:
    print('Você não pode financiar essa casa!')
else:
    print('Você terá de pagar {0} reais por mês para poder financiar a sua casa.'.format(prestacao))

# EXERCICIO 37

numero = int(input('Insira um número:'))
print('----------MENU----------')
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
opcao = int(input('Insira a sua opção\n'))

if opcao == 1:
    binario = bin(numero)
    print('O número {0} em binário é {1}.'.format(numero, binario))
elif opcao == 2:
    octal = oct(numero)
    print('O número {0} em octal é {1}.'.format(numero, octal))
else:
    hexa = hex(numero)
    print('O número {0} em hexadecimal é {1}.'.format(numero, hex))

# EXERCICIO 38

n1 = int(input('Insira o primeiro número:'))
n2 = int(input('Insira o segundo número:'))

if n1 > n2:
    print('{0} é o maior número.'.format(n1))
elif n2 > n1:
    print('{0} é o maior número.'.format(n2))
else:
    print('Eles são iguais.')

# EXERCICIO 39
idade = int(input('Insira a sua idade:'))
ano = 2025 - idade
if idade > 18:
    print('O seu ano de se alistar foi em {0}, {1} anos atrás.'.format(ano + 18, idade - 18))
elif idade == 18:
    print('É hora de se alistar!')
else:
    print('Você vai se alistar em {0}, daqui {1} anos'.format(ano + 18, 18 - idade))

# EXERCICIO 40
n1 = float(input('Insira a nota 1:'))
n2 = float(input('Insira a nota 2:'))
media = (n1 + n2) / 2
if media >= 7.0:
    print('APROVADO!')
elif media >= 5.0 and media <= 6.9:
    print('RECUPERACAO!')
else:
    print('REPROVADO!')

# EXERCICIO 41
ano = int(input("Insira o seu ano de nascimento:"))
idade = 2025 - ano
print('O atela tem {0} anos.'.format(idade))
if idade <= 9:
    print('Sua categoria é mirim.')
elif idade <= 14:
    print('Sua categoria é infantil.')
elif idade <= 19:
    print('Sua categoria é junior.')
elif idade <= 20:
    print('Sua categoria é sênior.')
else:
    print('Sua categoria é master.')

# EXERCICIO 42

n1 = int(input('Insira um número:'))
n2 = int(input('Insira o segundo número:'))
n3 = int(input('Insira o terceiro número:'))
if n1 > n2:
    if n1 > n3:
        maior = n1
        if n2 > n3:
            medio = n2
            menor = n3
            if menor + medio > maior:
                print('Esse triângulo é possível, ele é escaleno.')
            else:
                print('Esse triângulo não é possível')
        elif n3 > n2:
            medio = n3
            menor = n2
            if menor + medio > maior:
                print('Esse triângulo é possível, ele é escaleno.')
            else:
                print('Esse triângulo não é possível')
        else:
            if n3 + n2 > n1:
                print('O triângulo é possível, ele é isósceles.')
            else:
                print('O triângulo não é possível.')
        if n2 > n3:
            medio = n2
            menor = n3
            if menor + medio > maior:
                print('Esse triângulo é possível, ele é escaleno.')
            else:
                print('Esse triângulo não é possível')
        else:
            medio = n3
            menor = n2
            if menor + medio > maior:
                print('Esse triângulo é possível, ele é escaleno.')
            else:
                print('Esse triângulo não é possível')
    elif n3 > n1:
        medio = n1
        maior = n3
        menor = n2
        if menor + medio > maior:
                print('Esse triângulo é possível, ele é escaleno.')
        else:
            print('Esse triângulo não é possível')
    else:
        print('Esse triângulo não é possível.')
elif n2 > n1:
    if n2 > n3:
        maior = n2
        if n1 > n3:
            medio = n1
            menor = n3
            if menor + medio > maior:
                print('Esse triângulo é possível, ele é escaleno.')
            else:
                print('Esse triângulo não é possível')
        elif n3 > n1:
            medio = n3
            menor = n1
            if menor + medio > maior:
                print('Esse triângulo é possível, ele é escaleno.')
            else:
                print('Esse triângulo não é possível')
        else:
            if n3 + n1 > n2:
                print('O triângulo é possível, ele é isósceles.')
            else:
                print('O triângulo não é possível.')
    elif n3 > n2:
        menor = n1
        medio = n2
        maior = n3
        if menor + medio > maior:
            print('Esse triângulo é possível, ele é escaleno.')
        else:
            print('Esse triângulo não é possível')
    else:
        if n2 + n3 > n1:
            ('Esse triângulo é possível, ele é isósceles.')
        else:
            print('Esse triângulo não é possível.')
else:
    if n1 == n3:
        print('O triângulo é possível, ele é equilátero.')
    else:
            if n1 + n2 > n3:
                print('O triângulo é possível, ele é isósceles.')
            else:
                print('O triângulo não é possível.')

# EXERCICIO 43

peso = float(input('Insira o seu peso:'))
altura = float(input('Insira a sua altura:'))
imc = peso / altura ** 2
print('Seu imc é {:.1f}'.format(imc))
if imc > 40:
    print('Obesidade mórbida.')
elif imc > 30:
    print('Obesidade.')
elif imc > 25:
    print('Sobrepeso.')
elif imc > 18.4:
    print('Peso ideal.')
else:
    print('Abaixo do peso.')

# EXERCICIO 44

valor = float(input('Insira o valor do produto:'))
pag = str(input('Insira a forma de pagamento:'))
if pag == 'a vista':
    total = valor - (valor * 10 / 100)
elif pag == 'cartao':
    vezes = int(input('Em quantas vezes?'))
    if vezes == 1:
        total = valor - (valor * 5 / 100)
    elif vezes == 2:
        total = valor
    else:
       total = valor + (valor * 20 / 100)
print('O total a ser pago é {0}'.format(total))

# EXERCICIO 45

import random
opcao = str(input('Insira PE para pedra, PA para papel e T para tesoura.'))
lista = ['PE', 'PA', 'T']
computador = random.choice(lista)
print(computador)
if opcao == 'PE':
    if computador == 'PE':
        print('Empate')
    elif computador == 'PA':
        print('Você perdeu')
    else: print('Você ganhou')
elif opcao == 'PA':
    if computador == 'PE':
        print('Você ganhou')
    elif computador == 'PA':
        print('Empate')
    else: print('Empate')
else:
    if computador == 'PE':
        print('Você perdeu')
    elif computador == 'PA':
        print('Você ganhou')
    else: print('Empate')