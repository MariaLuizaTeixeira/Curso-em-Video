# OPERADORES

# EXERCICIO 5

numero = int(input('Insira um número: '))
print('O antecessor é {0} e o sucessor é {1}.'.format(numero - 1, numero + 1))

# EXERCICIO 6

numero = int(input('Insira um número: '))
print('O dobro é {0}, o triplo é {1} e a raiz quadrada é {2}.'.format(numero * 2, numero * 3, numero **(1/2)))

# EXERCICIO 7

n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número:'))
print('A média é igual a {:1f}.'.format((n1+n2)/2))

# EXERCICIO 8

numero = int(input('Insira uma quantia em metros: '))
print('O valor em centímetros é {0} e em milímetros é {1}.'.format(numero * 100, numero * 1000))

# EXERCICIO 9

numero = int(input('Insira um número:'))
print('TABUADA DO {0}:'.format(numero))
print('{0} x 1 = {1}'. format(numero, numero * 1))
print('{0} x 2 = {1}'. format(numero, numero * 2))
print('{0} x 3 = {1}'. format(numero, numero * 3))
print('{0} x 4 = {1}'. format(numero, numero * 4))
print('{0} x 5 = {1}'. format(numero, numero * 5))
print('{0} x 6 = {1}'. format(numero, numero * 6))
print('{0} x 7 = {1}'. format(numero, numero * 7))
print('{0} x 8 = {1}'. format(numero, numero * 8))
print('{0} x 9 = {1}'. format(numero, numero * 9))
print('{0} x 10 = {1}'. format(numero, numero * 10))

# EXERCICIO 10

dinheiro = float(input('Quantos reais você tem na carteira? '))
print('O seu dinheiro vale {0} dólares!'.format(dinheiro * 3.27))

# EXERCICIO 11

largura = float(input('Insira a largura(em metros): '))
altura = float(input('Insira a altura(em metros): '))
area = largura * altura
print('Serão necessários {0} baldes de tinta para pintar sua parede.'.format(area / 2))

# EXERCICIO 12

preco = float(input('Insira o preço do produto: '))
print('Com o desconto, o produto agora vale {0} reais.'.format(preco - (preco * 5 / 100)))

# EXERCICIO 13

salario = float(input('Insira o salario antigo: '))
print('O novo salário é de {0} reais.'.format(salario + (salario * 15 / 100)))

# EXERCICIO 14

temperatura = float(input('Insira a temperatura: '))
print('{0} graus Celcius são {1} graus Farenheit.'.format(temperatura,(9*temperatura)/ 5 + 32 ))

# EXERCICIO 15

dias = int(input('Por quantos dias o carro foi alugado?'))
km = int(input('Quantos kms foram percorridos? '))
dias_total = dias * 60
km_total = km * 0.15
print('Como foram rodados {0} kilômetros por {1} dias , o preço a ser pago é de {2}'.format(km, dias, dias_total + km_total))
