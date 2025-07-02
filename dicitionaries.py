# Dicionários
# Permitem armazenar dados em formato chave-valor

person = {
    'name': 'Luiz',
    'age': 29,
    'height': 1.81,
    'weight': 79,
    'is_dev': True
}

# print(person)

# # Acessando os items do dicionário

# print(f'Nome: {person['name']},\nIdade: {person['age']},\nAltura: {person['height']},\nPeso: {person['weight']},\nIs dev: {person['is_dev']}')

# Numero de elementos
# print(len(person))

# Atualizar dados do dicionario
# person['name'] = 'Luiz Henrique'

# print(f'Nome: {person['name']},\nIdade: {person['age']},\nAltura: {person['height']},\nPeso: {person['weight']},\nIs dev: {person['is_dev']}')

# Adicionar uma entrada

# person['city'] = 'Taubaté' # se a chave ainda nao existe, ela será criada

# print(person)

# Excluindo uma chave do dicionario

# del(person['city'])
# print('Cidade removida')
# print(person)

# Apagar tudo do dicionário

# person.clear()
# print(f'Dicionário person: {person}')

# Deletar o dicionário
# del person
# print(person)

# Listando apenas as chaves
print(person.keys())
# Listando apenas os valores
print(person.values())

# listando os itens - cada item vem dentro de uma tupla
for i in person.items():
    print(i)
    
for i, j in person.items():
    print(f'{i} : {j}')
