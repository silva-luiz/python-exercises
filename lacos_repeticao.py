# laços while, for e funcao range

x = 0

while x <= 5:
    print(x)
    x += 1

print('Fim do laço "while"')



list = [3,6,9,12]

for i in list:
    print(f'Lista aqui {i}')
print('Fim do laço "for" básico')


word = 'Python'

for letter in word:
    print(f'Letra aqui {letter}')
print('Fim do laço "for" com string')


y = 0

for y in range(6): # Neste caso, ele sempre começará o laço a partir de 0
    print(y)

print('Fim do laço "for"')

for y in range(5, 11): # Neste caso, ele começa a partir do valor que foi passado como primeiro argumento (1)
    print(y)

print('Fim do laço "for com range"')

# name = None # variavel sem valor/tipo definido

# while True:
#     print('Digite seu nome, ou X para sair: ')
#     name = input()
#     if (name == 'X' or name == 'x'):
#         break
#     print(f'Olá, {name}!')

# print('Você saiu.')


names = ('Luiz', 'Pedrão', 'Rafael', 'Nicolau')

for name in names:
    if name == 'Pedrão':
        continue # Pula o laço quando o nome for 'Pedrão' porém não sai od laço de repetição
    print(f'Olá, {name}!')