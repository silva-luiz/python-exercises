# variaveis

name = 'Luiz'; # str
age = 29; # int
is_dev = True; # bool
height = 1.81; # float

# as variáveis são case-sensitive, ou seja, 'name' e 'Name' são variáveis diferentes
# por convenção, nomes de variáveis são escritos em snake_case (letras minúsculas e com _ entre as palavras)
# é possível declarar várias variáveis na mesma linha, separando por vírgula

print(f'Olá, meu nome é {name}\ntenho {age} anos,\nsou dev? -> {is_dev}\ntenho {height}m de altura!');

media = 6;

nota_1 = 8;
nota_2 = 5;
nota_3 = 6.5;
nota_final = (nota_1 + nota_2 + nota_3) / 3;

print(f'A média final é {nota_final}');

if(nota_final >= media):
    print(f'Aprovado. Média: {nota_final}');
else:
    print(f'Reprovado. Média: {nota_final}');

print(type(media));
print(type(name));
print(type(age));
print(type(is_dev));
print(type(height));

# Função isinstance() verifica se uma variável é de um determinado tipo

print(isinstance(media, str)); # False
print(isinstance(media, int)); # True
