import random

tempo = int(input('Quantos anos tem o seu carro?'))
if tempo <= 3:
    print('Carro novo!')

else:
    print('Carro velho!')
print('FIM!')

nome = str(input('Insira o seu nome:'))
if nome == 'Malu':
    print('Que nome lindo!')

else:
    print('Seu nome é tão normal!')
print('Bom dia, {0}.'.format(nome))

nota1 = float(input('Insira a primeira nota:'))
nota2 = float(input('Insira a segunda nota:'))
media = (nota1 + nota2) / 2
print('Sua média foi: {0}.'.format(media))
if media < 6:
    print('Que nota feia :(')

else:
    print('Arrasou :)')

# EXERCICIO 28

numero = random.randint(0, 5)
print('Pensei em um número! Quer tentar adivinhar?')
tentativa = int(input('Insira sua tentativa aqui:'))

if numero == tentativa:
    print('Você acertou, parabéns!')

else:
    print('Você errou, o número era {0}'.format(numero))

# EXERCICIO 29

velocidade = int(input('Insira a velocidade do carro:'))
if velocidade > 80:
    print('Você passou do limite! Terá que pagar uma multa de {0} reais.'.format((velocidade - 80) * 7))

# EXERCICIO 30

numero = int(input('Insira um número:'))
if numero % 2 == 0:
    print('Esse número é par.')

else:
    print('Esse número é ímpar.')

# EXERCICIO 31

distancia = int(input('Insira sua distância em km:'))

if distancia < 200:
    preco_passagem = distancia * 0,50
    print('Como a sua distância é de {0} km, o preço da passagem é igual a {1} reais.'.format(distancia, preco_passagem))

else:
    preco_passagem = distancia * 0,45
    print('Como a sua distância é de {0} km, o preço da passagem é igual a {1} reais.'.format(distancia, preco_passagem))

# EXERCICIO 32

ano = int(input('Insira o ano:'))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano é bissexto!')
    
else:
    print('Esse ano não é bissexto.')

# EXERCICIO 33

n1 = int(input('Insira um número:'))
n2 = int(input('Insira o segundo número:'))
n3 = int(input('Insira o terceiro número:'))

if n1 > n2:
    if n1> n3:
        print('O {0} é o maior número.'.format(n1))

    else:
        print('O {0} é o maior número.'.format(n3))
else:
    if n2 > n3:
        print('O {0} é o maior número.'.format(n2))

# EXERCICIO 34

salario = int(input('Insira o seu salário:'))

if salario > 1250:
    salario += salario / 10
    print('Seu salário novo é de {0} reais.'.format(salario))

else: 
    salario += salario / 15
    print('Seu salário novo é de {0} reais.'.format(salario))

# EXERCICIO 35

n1 = int(input('Insira um número:'))
n2 = int(input('Insira o segundo número:'))
n3 = int(input('Insira o terceiro número:'))

if n1 > n2:
    if n1> n3:
        if n2 + n3 > n1:
            print('Esse triângulo é possível.')
        
        else:
            print('Esse triângulo não é possível.')

    else:
        if n2 + n1 > n3:
            print('Esse triângulo é possível.')
        
        else:
            print('Esse triângulo não é possível.')
else:
    if n2 > n3:
        if n1 + n3 > n2:
            print('Esse triângulo é possível.')
        
        else:
            print('Esse triângulo não é possível.')
    
    else:
        if n1 + n2 > n3:
            print('Esse triângulo é possível.')
        
        else:
            print('Esse triângulo não é possível.')




