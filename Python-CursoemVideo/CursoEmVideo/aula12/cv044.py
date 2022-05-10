
# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto

# – à vista no cartão: 5% de desconto

# – em até 2x no cartão: preço formal 

# – 3x ou mais no cartão: 20% de juros
print('-'*30)
print('Programa para auxiliar vendedores.')
print('-'*30)
total = float(input('Digite o total a pagar: '))
descontoAvista = (total) - (total * 0.10)
parcela = (total/3)
comissao01 = (total)-(total * 0.05) 
comissao02 = (total) - (total * 0.05) 
print(f'10% de desconto do total de {total} é:  {descontoAvista} R$')
print('O valor de cada parcela: %.2f R$'%parcela)
print(f'A comissão do vendedor no pagamento a vista é de 5%: {comissao01} R$')
print(f'A comissão do vendedor no pagamento parcelado é de 5%: {comissao02} R$')
