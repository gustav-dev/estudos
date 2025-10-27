# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

import math

print('[Calcule sua média e veja se passou de ano.]')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
media = (n1+n2)/2

if media >= 7:
    print('Sua média foi de {}.'.format(media))
    print('Parabéns! Você passou direto!')
elif media > 5 and 6.9:
    print('Sua média foi {}.'.format(media))
    print('Você está de recuperação. Procure seu professor e se prepare para uma nova prova.')
elif media < 5:
    print('Sua média foi {}.'.format(media))
    print('Infelizmente você ficou reprovado. Dedique-se mais no próximo ano.')