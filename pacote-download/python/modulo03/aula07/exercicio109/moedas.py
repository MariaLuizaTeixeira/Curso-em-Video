def aumentar(n, x, parametro=False):
    resposta = n + (n * x / 100)
    return resposta if parametro == False else moeda(n)
    
def diminuir(n, x, parametro=False):
    resposta = n - (n * x / 100)
    return resposta if parametro == False else moeda(n)

def dobro(n, parametro=False):
    resposta = n * 2
    return resposta if parametro == False else moeda(n)

def metade(n, parametro=False):
    resposta = n / 2
    return resposta if parametro == False else moeda(n)

def moeda(n, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')