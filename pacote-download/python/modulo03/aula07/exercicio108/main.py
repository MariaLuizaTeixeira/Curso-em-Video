import moedas

n = int(input('Digite o preço: R$ '))
print(f'A metade de {moedas.moeda(n)} é {moedas.moeda(moedas.metade(n))}')
print(f'O dobro de {moedas.moeda(n)} é {moedas.moeda(moedas.dobro(n))}')
print(f'Diminuindo 10% de {moedas.moeda(n)}, temos {moedas.moeda(moedas.diminuir(n, 10))}')
print(f'Aumentando 10% de {moedas.moeda(n)}, temos {moedas.moeda(moedas.aumentar(n, 10))}')