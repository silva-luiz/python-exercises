# operadores logicos

idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))

resultado = False

# # AND
# if (altura >= 1.80) and (idade >= 18):
#     resultado = True

# if (resultado):
#     print('Acesso permitido')
# else:
#     print('Acesso negado')


# # OR
# age = int(input('Insert your age: '))
# height = float(input('Insert your height: '))

# result = False

# if (age >= 1.80) or (height >= 18):
#     result = True

# if (result):
#     print('Access granted')
# else:
#     print('Access denied')


has_money = not False # O 'not' inverte o estado (!)

msg = f'Do you have any money? {has_money}'

print(msg)