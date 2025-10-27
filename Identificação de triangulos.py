# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

print('[ IDENTIFIQUE O TRIÂNGULO ]')

l1 = float(input('Insira o tamanho do primeiro lado: '))
l2 = float(input('Insira o tamanho do segundo lado: '))
l3 = float(input('Insira o tamanho do terceiro lado: '))

if l1 == l2 == l3:
    print('Você possui um triângulo equilátero. Pois todos os lados são igual.')

elif l1 != l2 and l2 != l3 and l1 != l3: #fiquei na dúvida de nao poder usar l1 != l2 != l3
    print('Seu triângulo é escaleno. Possui três lados diferentes.')
else:
    print('Os lados informados mostram um triângulo isósceles. Pois só tem dois lados iguais.')