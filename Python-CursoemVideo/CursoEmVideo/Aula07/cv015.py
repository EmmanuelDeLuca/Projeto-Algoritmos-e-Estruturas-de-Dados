alugado = int(input("Quantos dias alugados ?"))
km = float(input("Quantos km rodados ?"))

dia = alugado * 60
diakm = km * 0.15
soma = dia + diakm
print(f"total a pagar: {soma}")
