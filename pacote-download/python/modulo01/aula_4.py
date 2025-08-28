import math
import random
import playsound

numero = int(input('Digite um número: '))
raiz = math.sqrt(numero)
print('A raiz quadrada de {0} é {1}.'.format(numero, math.ceil(raiz)))

numero = random.randint(1, 10)
print(numero)

# EXERCICIO 16

numero = float(input('Insira um número: '))
print('A porção inteira desse número é {0}'.format(math.trunc(numero)))

# DESAFIO 17

cateto_oposto = int(input('Insira o comprimento do cateto oposto:'))
cateto_adjacente = int(input('Insira o comprimento do cateto adjacente:'))
hipotenusa   = math.hypot(cateto_adjacente, cateto_oposto)
print('Dado o valor dos catetos, o valor da hipotenusa é {0}'.format(hipotenusa))

# DESAFIO 18

angulo = int(input('Insira o valor do ângulo: '))
print('Como o ângulo é de {0} graus, o seno é {1}, o cosseno é {2}, e a tangente é {3}'.format(angulo, math.sin(math.radians(angulo)), math.cos(math.radians(angulo)), math.tan(math.radians(angulo))))

# DESAFIO 19

a1 = input('Insira o nome do aluno 1:')
a2 = input('Insira o nome do aluno 2:')
a3 = input('Insira o nome do aluno 3:')
a4 = input('Insira o nome do aluno 4:')
lista = [a1, a2, a3, a4]

print('O aluno sorteado é {}.'.format(random.choice(lista)))

# DESAFIO 20

a1 = str(input('Insira o nome do aluno 1: '))
a2 = str(input('Insira o nome do aluno 2: '))
a3 = str(input('Insira o nome do aluno 3: '))
a4 = str(input('Insira o nome do aluno 4: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação é: {0}.'.format(lista))

# DESAFIO 21

playsound.playsound('certo.mp3')
print('Você acertou!')
