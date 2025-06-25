# prints

print('Imprime a mensagem e muda de linha')
print('Imprime a mensagem e permanece na linha', end=' asdas')

# o end=' ' faz com que o \n seja substituído por um espaço em branco...
# também pode ser substituído por qualquer outro caractere

print('Agora essa é a última linha')

# String format

name = 'Luiz'
age = 29

print(f'Meu nome é {name}') # f-string para reduzir a quantidade de código e melhorar a legibilidade
print('Meu nome é {0}, e tenho {1} anos de idade'.format(name, age)) # 0 e 1 pegam as posições da lista do .format