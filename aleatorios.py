# numeros aleatorios
import random

# gerando um numero aleatorio
n = random.randint(1, 1000)
print(f'Número aleatório gerado entre 1 e 1000: {n}')

# gerando vários numeros aleatorios
for i in range(5):
    n = random.randint(1, 50)
    print(f'Número aleatório gerado entre 1 e 50: {n}')
    
# gerando um numero aleatorio com float (entre 0 e 1 - random.random)
n = random.random() # gera um numero aleatorio entre 0 e 1
print(round(n*10, 2)) # arredondando o valor aleatório entre 1 e 10, com duas casas depois da vírgula

valor = random.uniform(1, 100) # gerando um valor aleatorio float entre 1 e 100
print(round(valor, 3))

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# random.shuffle(L) # embaralha a lista
r = random.choice(L) # escolhe um elemento aleatório da lista
print(f'Lista embaralhada: {L}')
print(f'Elemento r escolhido da lista: {r}')

lista = []

for i in range(1, 11):
    lista.append(i)

for item in lista:
    print(item)
    
sorteado = random.choice(lista)
print(f'Número sorteado da lista: {sorteado}')