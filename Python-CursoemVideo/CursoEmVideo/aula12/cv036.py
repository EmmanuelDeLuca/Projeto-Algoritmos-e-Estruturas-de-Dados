# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casaV = float(input("Valor da casa R$ "))
salario = float(input("Seu salario R$ "))
anos = int(input("Em quantos anos deseja pagar: "))
prestaçao = casaV / ( anos*12)
porcento = salario*0.30/100

if( prestaçao > porcento):
    print("Para pagar uma casa de %d em %d anos a prestação será de R$ %.2f\nEmprestimo pode ser CONCEDIDO " % (casaV, anos, prestaçao) )
else:
    print("Para pagar uma casa de %d em %d anos a prestação será de R$ %.2f\nEmprestimo pode ser NEGADO " % (casaV, anos, prestaçao) )
    