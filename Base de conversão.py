#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número qualquer: '))
print('''Escolha uma das bases para conversão:
[1] = Converter para binário
[2] = Converter para octal
[3] = Converter para hexadecimal''')

opção = int(input('Sua opção é: '))

if opção == 1: #pq nao posso usar 'bi'?
    print('Sua conversão é {}.'.format(bin(opção)))
elif opção == 2:
    print('Sua converção é {}.'.format(oct(opção)))
elif opção == 3:
    print('Sua conversão é {}.'.format(hex(opção)))
else:
    print('Opção inválida.')