# Sets
# Armazenam apenas itens não duplicados, e não podem ser modificados - imutável
# Pode ter itens de qualquer tipo

# planeta_anao = {'Plutao', 'Ceres', 'Eris', 'Haumea', 'Makemake'}

# print(planeta_anao)

# print(len(planeta_anao))

# # Contém?
# # print('Ceres' in planeta_anao)
# # Não contém?
# # print('Moon' not in planeta_anao)

# for astro in planeta_anao:
#     print(astro.upper()) # Imprime tudo em maiuscula
    
# astros = ['Lua', 'Vênus', 'Sirius', 'Sol']

# print(astros)
# astros.append('Marte')
# # Transformando uma 'list' em um 'set'
# astrosSet = set(astros)
# print(astrosSet)

astros1 = {'Lua', 'Vênus', 'Sirius', 'Sol'}
astros2 = {'Lua', 'Vênus', 'Sirius', 'Sol', 'Terra'}

print(astros1 == astros2)
print(astros1 != astros2)

print(astros1 | astros2) # União de conjuntos utilizando o | (valores duplicados são mostrados apenas uma vez)

astros3 = astros1.union(astros2)
print(astros3) # Também une os dois criando um novo conjunto

astros3.add('Saturno')
astros3.discard('Terra') # Remove o elemento escolhido
astros3.pop() # Remove um elemento
print(astros3)
astros3.clear() # Limpa o Set
print(astros3)
