# Calcular média

n1 = n2 = 0
media = 0

print('Cálculo de média do Estudante')

n1 = float(input('Digite a primeira Nota: '))
n2 = float(input('Digite a segunda Nota: '))

media = (n1+ n2) / 2

print(f'A média do aluno é: {media:.1f}')

if (media >= 7):
    print('O aluno foi aprovado!!')
else:
    print('O aluno foi reprovado!!')