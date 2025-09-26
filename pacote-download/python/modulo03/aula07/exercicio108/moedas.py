def aumentar(n, x):
    resposta = n + (n * x / 100)
    return resposta
    
def diminuir(n, x):
    resposta = n - (n * x / 100)
    print(resposta)
    return resposta
        
def dobro(n):
    resposta = n * 2
    return resposta

def metade(n):
    resposta = n / 2
    return resposta

def moeda(n, moeda='R$'):
    return f'R$ {n},00'