from utilidadesCeV import moedas
def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg))
        if entrada.isalpha():
            print('ERRO! Digite um número inteiro válido')
        else:
            valido = True
            return int(entrada)
