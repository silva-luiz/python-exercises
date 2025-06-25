# Funções matematicas

import math 

# Funções built in (internas)

valores = [-1, 0, 3, 5, 9, 15, 23, 14]

print(max(valores))
print(min(valores))

a = -5
b = 4

print(abs(a)) # Valor absoluto
print(abs(b)) # Valor absoluto

print(pow(a, b)) # 'a' elevado a 'b'

c = 2.75234

print(round(c, 2)) # arredonda c com duas casas decimais

# Funções matemáticas importadas do módulo math

print(math.pi)
print(math.e)

x = 8
y = 100

raiz = math.sqrt(8)
print(math.ceil(raiz)) # Arredonda para cima
print(math.floor(raiz)) # Arredonda para baixo

logaritmo = math.log10(y)
print(logaritmo)
print(math.factorial(x))