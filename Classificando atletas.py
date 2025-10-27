#A Confederação Nacional de Natação precisa de um programa que leia
#o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

print('[ IDENTIFIQUE A SUA CATEGORIA ]')
idade = int(input('Qual a sua idade? '))

if 5 <= idade < 9:
    print('Pela sua idade de {} anos, sua categoria é a Mirim.'.format(idade))
elif 10 <= idade <= 10:
    print('Pela sua idade de {} anos, sua categoria é a Infantil.'.format(idade))
elif 15 <= idade <= 19:
    print('Pela sua idade de {} anos, sua categoria é a Júnior.'.format(idade))
elif 20 <= idade <= 25:
    print('Pela sua idade de {} anos, sua categoria é a Sênior.'.format(idade))
elif idade > 25:
#else:
    print('Pela sua idade de {} anos, sua categoria é a Master.'.format(idade))