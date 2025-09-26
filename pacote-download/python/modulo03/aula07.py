def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f*=c
    return f
def dobro(n):
    return n * 2

num = int(input('Digite um valor:'))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')