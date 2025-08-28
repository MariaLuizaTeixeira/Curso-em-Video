teste = list()
galera = list()
teste.append('Gustavo')
teste.append(40)
print(teste)
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
print(galera)
print(teste)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[0][0])
print(galera[2][1])
for p in galera:
    print(p)
for p in galera:
    print(p[0])
galera = list()
dado = list()
for i in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

# EXERCICIO 84
pessoas = list()
dados = list()
cont = 0
maior = list()
menor = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    opcao = str(input('Deseja continuar? [N para parar]'))
    if opcao == 'N':
        break
maior = pessoas[0]
menor = pessoas[0]
print(maior)
print(len(pessoas))
while cont < len(pessoas) - 1:
    print(f'cont é {cont}')
    if maior[1] < pessoas[cont + 1][1]:
        maior = pessoas[cont + 1]
    if menor[1] > pessoas[cont + 1][1]:
        menor = pessoas[cont + 1]
    cont+=1
print(f'a) Há {len(pessoas)} pessoas cadastradas.')
print(f'b) A(s) pessoa(s) mais pesada(s) é(são) {maior[0]}.')
print(f'b) A(s) pessoa(s) mais leve(s) é(são) {menor[0]}.')

# EXERCICIO 85
lista = [[], []]
for i in range(0,7):
    i = int(input('Insira um valor:'))
    if i % 2 == 0:
        if len(lista[0]) == 0 or i > lista[0][-1]:
            lista[0].append(i)
        else:
            pos = 0
            while pos < len(lista):
                if i <= lista[0][pos]:
                    lista[0].insert(pos, i)
                    break
            pos+=1
    else:
        if len(lista[1]) == 0 or i > lista[1][-1]:
            lista[1].append(i)
        else:
            pos = 0
            while pos < len(lista):
                if i <= lista[1][pos]:
                    lista[1].insert(pos, i)
                    break
            pos+=1
print(lista)

# EXERCICIO 86

lista = [[], [], []]
for i in range (0,3):
    for j in range (0,3):
        j = int(input('Insira um número: '))
        lista[i].append(j)
print(lista)

# EXERCICIO 87

pares = coluna = 0
lista = [[], [], []]
for i in range (0,3):
    cont = 0
    for j in range (0,3):
        j = int(input('Insira um número: '))
        lista[i].append(j)
        if j % 2 == 0:
            pares+=j
        if i == 1:
            if cont == 0:
                maior = j
            else:
                if j > maior:
                    maior = j
for i in range(0,3):
    coluna+= lista[i][2]
print(f'a) A soma dos pares é {pares}.')
print(f'b) A soma dos valores da terceira coluna é {coluna}.')
print(f'c) O maior valor da segunda linha é {maior}.')

# EXERCICIO 88

import random
palpites = list()
dados = list()
jogos = int(input('Insira a quantidade de jogos a ser gerada:'))
for i in range (0, jogos):
    for i in range(0, 6):
        palpites.append(random.randint(1, 60))
    dados.append(palpites[:])
    palpites.clear()
print(dados)

# EXERCICIO 89

alunos = list()
aluno = list()
while True:
    nome = str(input('Insira o nome do aluno: '))
    n1 = float(input('Insira a nota 1 do aluno: '))
    n2 = float(input('Insira a nota 2 do aluno: '))
    media = round((n1 + n2) / 2, 2)
    opcao = str(input('Deseja continuar? [S/N]'))
    aluno = [nome, n1, n2, media]
    alunos.append(aluno[:])
    aluno.clear()
    if opcao in 'nN':
        break
print('---------- BOLETINS ----------')
print('NOME        MÉDIA')
for i in range(0, len(alunos)):
    print(f'{alunos[i][0]} -----> {alunos[i][3]}')
while True:
    opcao1 = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opcao1 == 999:
        break
    else:
        print(f'Notas de {alunos[opcao1][0]} são: {alunos[opcao1][1]} e {alunos[opcao1][2]}.')

