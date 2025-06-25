# laços de repetição encadeados
# para percorrer uma matriz ou tabela por exemplo

import random

# for col in range(1, 6):
#     print(f'\n>Coluna #{col}')
#     for row in range(1,6):
#         print(f'>>Linha #{row}')


for A in range(1,3):
    print(f'\nConjunto {A}')
    for B in range(6):
        num = random.randint(1, 60) # numeros aleatorios entre 1 e 100
        # if(num % 2 == 0):
        #     print(f'Este número é par: {num}')
        print(f'>> Número {B+1} do conjunto {A}: {num}')