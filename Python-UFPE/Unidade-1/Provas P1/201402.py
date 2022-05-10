# Faça um programa Python para ler uma tabela de pessoas onde:
#  Cada pessoa tem um cpf (long), um nome (String) e um salário (float).
#  A leitura da tabela pára com um cpf que não seja positivo. 
# Depois o usuário informará um intervalo de salários, ou seja, os limites inferior e superior do
# intervalo. Ambos devem ser positivos, mas o limite inferior pode ser zero. Além disto, o
# limite inferior do intervalo deve ser menor do que o limite superior. Caso alguma destas
# restrições seja violada, o programa deve informar o erro ao usuário e pedir os dados
# novamentre. De posse de um intervalo correto, o programa deve imprimir os dados das
# pessoas que se enquadram no intervalo, seguidos pelo número de pessoas do intervalo, e pela
# média dos salários destas pessoas.

pessoas = {}

cpfPessoa = int(input("Digite seu CPF (Tem que ser positivo): "))
while cpfPessoa < 1:
    cpfPessoa = int(input("Digite seu CPF novamente, lembrando tem que ser maior que 0 (Tem que ser positivo): "))

while cpfPessoa != 0:
    nomePessoa = input("Digite seu nome: ")
    salarioPessoa = float(input("Diga seu salario: "))
    pessoas[cpfPessoa] = (nomePessoa, salarioPessoa)

    while (cpfPessoa < 0) or (cpfPessoa in pessoas):
        cpfPessoa = int(input("Digite seu CPF (0 para o programa): "))
print(pessoas)




limite_inferior = float(input("Limite inferior salarial: "))
while limite_inferior < 0:
    limite_inferior = float(input("Limite inferior salarial: "))

limite_superior = float(input("Limite supeior salarial: "))
while  limite_superior < 0:
    limite_superior = float(input("Limite supeior salarial: "))


if limite_inferior < limite_superior:
    quantidade_pessoas = 0
    salario = 0
    
    for i in pessoas:
        if pessoas[i][1] >= limite_inferior and pessoas[i][1] <= limite_superior:
            quantidade_pessoas += 1
            salario+= pessoas[i][1] 
            media = salario/quantidade_pessoas
        print('Pessoas dentro do limite:  ',pessoas[i][0], )
        print('Media do salario: ', media)

    # cpfPessoa = int(input("Digite 0:  "))
        
print(f'Quantidade de pessoas dentro do limites {quantidade_pessoas}')


