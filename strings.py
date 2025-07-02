# String

# Docstrings
# Documentar trechos do código (não são apenas comentários)
# Cria-se colocando tres aspas """

texto = """
Este é um Docstring, uma espécie de documentação que podemos inserir dentro de um módulo,
função, ou classe no Python, entre outros locais.
    Pode ocupar diversas linhas e respeita o deslocamento (tab, espaços, etc...).
Deve-se usar apenas quando é necessário explicar uma definição longa. Não é recomendado usar
como comentário.
"""

print(texto)

# p = 'Luiz Henrique'

# print(p.startswith('s')) # Começa com a string escolhida
# print(p.startswith('Luiz')) # Começa com a string escolhida
# print(p.endswith('que')) # Finaliza com a string escolhida

# fruta = 'abacate'

# print(fruta)

# print(fruta.rjust(25, '.')) # alinhar 25 pontos à direita
# print(fruta.ljust(25, '.')) # alinhar 25 espaços à esquerda
# print(fruta.center(25, '.')) # centralizar

# email = input('Digite seu e-mail corporativo: ')

# at = email.find('@')
# print(at)

# user = email[0:at]
# domain = email[at+1:]

# print(user)
# print(domain)

# name = 'Luiz'
# surname = 'Silva'

# full_name = name + ' ' + surname

# letter = name[2]

# print(letter)
# print(len(name))
# print(full_name)

# phrase = 'Parabéns, boa sorte lá!'

# words = phrase.split()

# print(words)
# for word in words:
#     print(word)
    
# for letra in phrase:
#     print(letra)

# print(phrase[10:20]) # slice