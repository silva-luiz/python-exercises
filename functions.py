# Funções

# Criando uma função

# def <nome_funcao> ([argumentos]):
#     <instrucoes da funcao>

# def message(name): # Função que recebe um argumento
#     print('Surprise!')
#     print(f'First function {name}!')
    
# message('Luiz')


# def soma(a, b):
#     print(a+b)

# soma(3,5)

# def mult(x, y):
#     return x * y # Função encerra aqui no return

# a = 5
# b = 8
# c = mult(a, b)

# print(f'O produto de "a" e "b" é {c}')

def div(k, j):
    if(j == 0):
        return 'Erro - Divisão por zero meu parça'
    return k / j

def quadrado(val):
    quadrados = []
    for x in val:
        quadrados.append(x ** 2)
    return quadrados

if __name__ == '__main__':

    # a = int(input('Digite o valor do dividendo: \n'))
    # b = int(input('Digite o valor do divisor: \n'))
    # c = div(a, b)

    # print(c)
    
    values = [1, 3, 5, 7, 9]
    r = quadrado(values)
    
    for g in r:
        print(g)