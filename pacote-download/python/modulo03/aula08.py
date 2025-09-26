"""
try:
    a = int(input("Insira um número: "))
    b = int(input("Insira um número: "))
    r = a / b

    # except Exception as erro:
   # print(f"PROBLEMA! O erro encontrado foi {erro.__class__}.")

except (ValueError, TypeError):
    print(f"Tivemos um erro com o dado digitado.")
    
except (ZeroDivisionError):
    print(f"Não é possível realizar divisão por 0.")
    
except (KeyboardInterrupt):
    print(f"O usuário preferiu não informar os dados.")
    
except Exception as erro:
    print(f"Erro {erro}.")
else:
    print(f"O resultado é {r}.")
    
finally:
    print('FIM DO PROGRAMA!')
"""
# EXERCICIO 113
def leiaInt(num):
    while True:
        try:
            num = input('Insira um número real:') 
        except (ValueError, TypeError):
            print(f"Tivemos um erro com o dado digitado.")
            
        except (ZeroDivisionError):
            print(f"Não é possível realizar divisão por 0.")
            
        except (KeyboardInterrupt):
            print(f"O usuário preferiu não informar os dados.")

        except Exception as erro:
    print(f"Erro {erro}.")
        num = input('Insira um número inteiro:')
        if num.isnumeric() == False:
            print('ERRO! Digite um número inteiro válido!')
            num = input('Insira um número inteiro:')
        else: 
            break

def leiaFloat(numero):
    while numero.isnumeric() == False:
        print('ERRO! Digite um número real válido!')
        numero = input('Insira um número real:')
    

else:
    print(f'O número digitado foi {num}.', end=" ")
    print(f'O número digitado foi {numero}.')
finally:
    print('FIM DO PROGRAMA!')
