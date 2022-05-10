from datetime import datetime
dados = {}

dados['Nome'] = str(input("Qual seu nome? "))
nasc = int(input("Digite seu ano de nascimento: "))
dados['idade'] = datetime.now().year - nasc

dados['Carteira'] = int(input("Possui carteira de trabalho ? (Digite 0 pra não)"))

if dados['Carteira'] != 0:
    dados['anoContratação'] = int(input("Ano de contratação: "))

    dados['Salario'] = float(input("Qual seu salario ? "))

    dados['aposentadoria'] = dados['idade'] + ((dados['anoContratação']+35) - datetime.now().year)

for i, o in dados.items():
    
    print(f' -{i} tem valor {o}')


