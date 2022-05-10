pessoas = {}

codigoDePessoa = int(input("Digite seu codigo(0 Parar o programa): "))
while codigoDePessoa < 1:
    codigoDePessoa = int(input("Erro! Digite um codigo valido(Codigo > 0): "))

while codigoDePessoa != 0:
    nomeDaPessoa = input("Digite seu nome: ")
    salarioDaPessoa = float(input("Digite seu salario: "))
    while salarioDaPessoa < 1:
        salarioDaPessoa = float(input("error! Digite seu salario: "))
    
    pessoas[codigoDePessoa] = (nomeDaPessoa, salarioDaPessoa)

    codigoDePessoa = int(input("Digite seu codigo(0 Parar o programa): "))
    while (codigoDePessoa < 0) or (codigoDePessoa in pessoas):
        codigoDePessoa = int(input("Digite seu codigo(0 Parar o programa): "))
    
print(f'Pessoa cadastrada com sucesso. {pessoas}')
valorMax= float(input("Digite um valor maximo de salário: "))
while valorMax < 0:
    valorMax= float(input("Digite um valor maximo de salário: "))
numeroDePessoas = 0
while valorMax !=0:
    for i in pessoas:
        if pessoas[i][1] < valorMax:
            numeroDePessoas = numeroDePessoas +1 
            print('  ',i, numeroDePessoas, pessoas[i])
    valorMax= float(input("Deseja para o programa ? (Digite 0) "))
print('Fim do programa')
    
   
