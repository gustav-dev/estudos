# Exercício Python: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos
anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

nome = str(input('Qual o seu nome completo? '))
conjuge = str(input('Qual o nome do conjuge? '))
renda = (float(input('Qual o valor da renda familiar? ')))
valor_do_imovel = int(input('Qual o valor do imóvel em vista? '))
financiamento = float(input('Qual o valor do financiamento desejado? '))
meses = int(input('Pretende dividir o financiamento em quantos meses? '))

print(nome)
print(conjuge)
print('Renda familiar de {}reais.'.format(renda))
print('O valor do imovel desejado é de {}reais.'.format(valor_do_imovel))
print('O valor pedido para financiamento é de {}reais.'.format(financiamento))
print('O cliente pretende pagar em até {} meses.'.format(meses))

limite_renda = renda*0.30
prestacao = financiamento/meses


if prestacao >= limite_renda:
    print('Seu empréstimo foi negado, pois o valor pedido de R${} ultrapassa 30% da renda familiar nas prestações.'.format(renda))
elif prestacao <= limite_renda:

    print('Parabéns! O empréstimo foi aceito.')
