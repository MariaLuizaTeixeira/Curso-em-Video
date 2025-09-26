import moedas

n = int(input('Digite o preço: R$ '))
print(f'A metade de {n} é {moedas.metade(n)}')
print(f'O dobro de {n} é {moedas.dobro(n)}')
print(f'Diminuindo 10% de {n}, temos {moedas.diminuir(n, 10)}')
print(f'Aumentando 10% de {n}, temos {moedas.aumentar(n, 10)}')