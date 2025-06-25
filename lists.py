# Listas
# representa uma sequencia de valores

# notas = [8.5, 9.0, 6.0, 2.5, 10.0]

# print(notas) # Print da lista completa
# print(notas[0]) # Print do primeiro elemento
# print(notas[1]) # Print do segundo elemento...
# print(notas[-1]) # Print do ultimo elemento

# n1 = [4, 6, 8, 0, 3]
# n2 = [1, 6 ,3, 0 ,12]

# valores = n1 + n2 # Concatena em uma nova lista
# print(valores)

# new_value = valores[0] + 10 # Altera o primeiro elemento da lista somando 10
# valores[0] = 22
# print(len(valores)) # Imprime o tamanho da lista
# print(sorted(valores)) # Versao ordenada da lista
# print(sorted(valores, reverse=True)) # Versao ordenada reversamente
# print(sum(valores)) # soma dos valores da lista
# print(max(valores)) # Maior valor da lista
# print(min(valores)) # Menor valor da lista

# valores.append('100') # adiciona um novo valor ao final da lista
# valores.insert(2, 10)
# print(valores)
# valores.pop() # remove o ultimo valor da lista
# valores.pop(5) # remove o valor do indice 2 
# print(valores)

# planetas = ['Terra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Netuno']

# for planeta in planetas: # Percorrendo a lista
#     print(planeta)

drinks = []

for i in range(5):
    drink = input('Digite uma bebida favorita: ')
    drinks.append(drink)
print('Bebidas favoritas:')

drinks.sort()

for drink in drinks:
    print(drink)   