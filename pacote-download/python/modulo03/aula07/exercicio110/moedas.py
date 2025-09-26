def aumentar(n, aumento):
    resposta = n + (n * aumento / 100)
    return moeda(resposta)
    
def diminuir(n, diminuicao):
    resposta = n - (n * diminuicao / 100)
    return moeda(resposta)

def dobro(n):
    resposta = n * 2
    return moeda(resposta)

def metade(n):
    resposta = n / 2
    return moeda(resposta)

def moeda(n, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')

def resumo(n, aumento, diminuicao):
    print('-'*10)
    print('RESUMO DO VALOR')
    print('-'*10)
    print(f'Preço analisado:       {moeda(n)}')
    print(f'Dobro do preço:       {dobro(n)}')
    print(f'Metade do preço:       {metade(n)}')
    print(f'{aumento}% de aumento:       {aumentar(n, aumento)}')
    print(f'{diminuicao}% de diminuição:       {diminuir(n, diminuicao)}')