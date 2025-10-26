# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais

n1 = int(input('Digite um número inteiro qualquer: '))
n2 = int(input('Digite outro número inteiro qualquer: '))

if n1 > n2:
    print('O primeiro número inserido é maior que o segundo inserido.')
elif n1 < n2:
    print('O primeiro número inserido é menor que o segundo inserido.')
else:
    print('O primeiro e o segundo inserido são iguais. Não existe maior ou menor.')

