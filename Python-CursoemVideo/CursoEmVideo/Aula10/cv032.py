ano = int(input("Digite o ano que deseja saber se é bissexto ou não: "))

if ano%4 == 0:
    print(f"ano de {ano} é bissexto")
else:
    print(f"o ano de {ano} não é bissexto")