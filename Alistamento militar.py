# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano_atual = date.today().year

print('ALISTAMENTO MILITAR')
nasc = int(input('Qual o ano do seu nascimento? '))
idade = ano_atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, ano_atual))


if idade == 18:
    print('Você esta no ano do alistamento. Procure uma instituição do exército em sua cidade.')

elif idade < 18:
    falta = 18 - idade
    ano_alistamento = ano_atual + falta
    print('Você ainda não precisa se alistar. Faltam {} anos para seu alistamento.'.format(falta))
    print('Seu alistamento será em {}.'.format(ano_alistamento))

elif idade > 18:
    passou = idade - 18
    ano_alistamento = ano_atual - passou
    print('Você já deveria ter se alistado em {}.'.format(ano_alistamento))
    print('Procure imediatamente uma instituição do exército para regularizar a sua situação.'.format(passou))