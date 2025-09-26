import moedas

n = int(input('Digite o preço: R$ '))
print(f'A metade de {moedas.moeda(n)} é {moedas.metade(n, True)}')
print(f'O dobro de {moedas.moeda(n)} é {moedas.dobro(n, True)}')
print(f'Diminuindo 10% de {moedas.moeda(n)}, temos {moedas.diminuir(n, 10, False)}')
print(f'Aumentando 10% de {moedas.moeda(n)}, temos {moedas.aumentar(n, 10, False)}')