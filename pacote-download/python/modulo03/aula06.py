help(print)
print(input.__doc__)

def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')
help(contador)

def somar(a=0, b=0, c=0):
    """
    Soma três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return: sem retorno
    """
    s = a + b + c
    print(f'A soma vale {s}')
somar(3, 2, 5)
somar(8, 4)

# EXERCICIO 101
def voto(ano):
    if 2025 - ano >= 18:
        print('Obrigatório')
    elif 2025 - ano >= 16:
        print('Opcional')
    else:
        print('Negado')
voto(2009)
voto(2000)
voto(2020)

# EXERCICIO 102
def fatorial(numero, show=False):
    for i in range(numero - 1, 0, -1):
        anterior = numero
        numero*=i
        if show == True:
            print(f'{anterior} x {i} = {numero}')
    print(f'O resultado é {numero}.')
fatorial(5)

# EXERCICIO 103
def ficha(nome='', gols =0):
    if nome.strip() == '':
        nome = '<desconhecido>'
    print(f'O jogador {nome} fez {gols} gols no campeonato')
nome = str(input('Insira o nome do jogador:'))
gols = int(input('Insira a quantidade de gol(s) que o jogador fez:'))
ficha(nome, gols)

# EXERCICIO 104
def leiaint(num):
    while num.isnumeric() == False:
        print('ERRO! Digite um número inteiro válido')
        num = input('Insira um número:')
    print(f'O número digitado foi {num}.')
num = input('Insira um número:')
leiaint(num)

# EXERCICIO 105

def notas(* num, bool=''):
    cont = maior = soma = 0
    for valor in num:
        print(f'{valor}', end=' ')
        if cont == 0:
            maior = valor
            menor = valor
        else:
            if valor > maior:
                maior = valor
                menor = valor
            if menor < valor:
                valor = menor
        soma+=valor
        cont+=1
        media = soma / cont
    if bool == True:
        if media >=8:
            situacao = 'boa'
        elif media >=6:
            situacao = 'media'
        else:
            situacao = 'ruim'
        dic = [cont, maior, menor, media, situacao]
    else:
        dic = [cont, maior, menor, media]
    
    return dic
resp = notas(10, 10, 10, True)
print(resp)



