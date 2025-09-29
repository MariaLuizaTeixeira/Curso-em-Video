pessoas = {'nome': 'Gustavo', 'sexo' : 'M', 'idade' : 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
for k in pessoas.keys():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 85

estado1 = {'uf' : 'Rio de Janeiro', 'sigla' : 'RJ'}
estado2 = {'uf' : 'Paraná', 'sigla' : 'PR'}
brasil = []
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[1])
print(brasil[0]['uf'])

estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado:'))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')

# EXERCICIO 90
aluna = dict()
aluna['nome'] = str(input('Insira o nome da aluna(o): '))
aluna['media'] = float(input('Insira a média da aluna(o): '))
if aluna['media'] >= 6.0:
    print(f'{aluna["nome"]} está aprovada(o). ')
else:
    print(f'{aluna["nome"]} está reprovada(o). ')

# EXERCICIO 91
import random
x = 1
jogadores = {'jogador1' : 0, 'jogador2' : 0, 'jogador3' : 0, 'jogador4' : 0}
print('Valores sorteados:\n')
for j in jogadores:
    jogadores[j] = random.randint(1, 6)
    print(f'O {j} tirou {jogadores[j]}')
sorted(jogadores)
print(jogadores)
for j, p in jogadores.items():
    print(f'Em {x}° lugar: {j} com {p} pontos.')
    x+=1

# EXERCICIO 92
pessoa = dict()
pessoa['nome'] = str(input('Insira o seu nome: '))
pessoa['idade'] = int(input('Insira a sua idade: '))
pessoa['ano_nascimento'] = int(input('Insira o seu ano de nascimento: '))
pessoa['carteira'] = int(input('Insira o número da carteira de trabalho: (o não tem): '))

if pessoa['carteira'] != 0:
    pessoa['ano_contratacao'] = int(input('Insira o seu ano de contratação:'))
    pessoa['salario'] = float(input('Insira o seu salário:'))
    print('Faltam {0} anos para você se aposentar.'.format(62 - 2025 + (pessoa['ano_nascimento'])))

# EXERCICIO 93
x = 1
tot = 0
jogadora = dict()
jogadora['nome'] = str(input('Insira o nome da jogadora:'))
jogos = int(input('Insira a quantidades de partidas que a jogadora jogou:'))
partidas = list()
for i in range(0, jogos):
    a = int(input(f'Insira a quantidade de gols que ela fez na partida {x}:'))
    partidas.append(a)
    x+=1
    tot+=a
jogadora['gols'] = partidas
print(jogadora)
print(f'Ela fez um total de {tot} gols.')

# EXERCICIO 94
pessoa = dict()
pessoas = list()
mulheres = list()
acima = list()
media = n = 0
opcao = 1

while opcao != 0:
    pessoa['nome'] = str(input('Insira o nome:'))
    pessoa['sexo'] = str(input('Insira o sexo:'))
    pessoa['idade'] = str(input('Insira a idade:'))
    pessoas.append(pessoa[:])
    opcao = int(input('Insira 0 para para e qualquer outro número para continuar:'))
    media+=pessoa['idade']
    n +=1
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa[:])
print('A média de idade é {0}'.format(media / n))
print('As mulheres são: ')
for i in mulheres:
    print(mulheres[i]['nome'], end=' ')
for i in pessoas:
    if pessoas[i]['idade'] > media / n:
        print(pessoas[i]['nome'], end=' ')

