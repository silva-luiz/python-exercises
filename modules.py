# Imports sempre no inicio do script

# import math  -> importa o módulo inteiro
# import math as m -> importa o módulo com um alias escolhido pelo usuário

from math import pi, sqrt # importa somente funções específicas do módulo



if __name__ == '__main__': # por convenção, este é o ponto de entrada do módulo, ou seja, o ponto de início da execução do script
    print('Módulo executado diretamente')

# print(f'Valor de pi: {math.pi}') # modulo + nome da função (math.pi)
print(f'Valor de pi: {pi}') # nao precisa do nome do módulo

# print(f'Raiz quadrada de 25: {math.sqrt(25)}') # modulo + nome da função (math.sqrt(x))
print(f'Raiz quadrada de 25: {sqrt(25)}')  # nao precisa do nome do módulo