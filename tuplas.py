# Tuplas
# Tuplas permitem varios tipos de dados armazenados
# mas sao imutaveis, ou seja, nao pode ser alterada depois de criada

tupla = (2, 4, 6, 8)

# tupla[1] = 5 # Essa linha causaria um erro, pois uma tupla nao pode ser alterada 

print(tupla)

halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn')
elementos = halogenios + gases_nobres

print(len(halogenios))
print(halogenios[2])

print(elementos)
print('F' in halogenios)
print('F' in gases_nobres)
print('F' in elementos)

# Operações nao disponiveis em tuplas: 
# .sort(), .reverse(), .append(), .insert(), .remove(), .pop()

print('Elementos quimicos da tupla: ')
for elemento in elementos:
    print(elemento)

# Criando uma lista a partir de uma tupla
grupo17 = list(halogenios)
print(grupo17) # Agora a lista pode ser manuseada

# Criando uma tupla a partir de uma lista
gases_tupla = tuple(gases_nobres)
print(gases_tupla)  # Agora a tupla pode ser usada como uma tupla

gases_ordenados = sorted(gases_tupla)
print(gases_ordenados)  # A tupla original nao foi alterada, mas a lista ordenada foi criada