# operadores aritméticos

x = y = z = 0

x = 7
y = 9

z = x + y
print(f'A soma dos dois valores é {z}');

# adicionando os valores por input

a = int(input('Digite o primeiro valor: ')) # se nao colocar o int(), o resultado do input será uma string
b = int(input('Digite o segundo valor: '))

c = a + b
print(f'A soma de "A" e "B" é: {c}')

# Operador de comparação

d = e = 0

d = int(input('Digite o valor de D: '))
e = int(input('Digite o valor de E: '))

if d != e:
    print(f'Valores diferentes: {d} e {e}')

if d == e:
    print(f'Valores iguais: {d} e {e}')


