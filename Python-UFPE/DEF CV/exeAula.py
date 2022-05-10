# def mostralinha():
#     print("-"*30 )
# mostralinha()
# print('    Sismtemas de alunos          ')
# mostralinha()

# Parametros
# def mensagem(msg):
#     print('-'*30)
#     print(msg)
#     print('-'*30)
# mensagem('  SISTEMAS DE ALUNOS')
# mensagem('  SISTEMAS DE ALUNOS')
# mensagem('  SISTEMAS DE ALUNOS')

# Parte Prática
# def soma(a,b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'A soma A + B = {s}') 
# soma(2,1)

# Enpacotamento
# def contador(*núm):
#     for i in núm:
#         print(i)

# contador(2,3,4)
# contador(1,2)
# contador(2,3,4,5,6,7)

# def contador(*núm):
#     tam = len(núm)
#     print(núm, tam)

# contador(2,3,4)
# contador(1,2)
# contador(2,3,4,5,6,7)

# Dobra valores

# def dobra(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos]*=2
#         pos+=1
# valores = [1,2,3,4,5,6,7]
# dobra(valores)
# print(valores )
# Crie uma função que pede dois números, faz a soma e exibe o 
# resultado, através de uma função. O usuário pode executar a função 
# quantas vezes desejar.

# def somar():
#     numA = float(input("Digite o valor de A: "))
#     numB = float(input("Digite o valor de B: "))
#     somar = numA + numB
#     print(f'soma dos valors {numA} e {numB} é : {somar}')

# i = 1
# while i:
#     if(i):
#         somar()
# i = int(input("Digite 0 se deseja encerrar o programa: "))

# Faça uma calculadora, usando funções. O script pergunta qual 
# operação o usuário deseja rodar (soma, subtração, multiplicação ou 
# divisão) e executa a operação.
# A calculadora deve ser executada quantas vezes o usuário desejar. 

# def somar():
#     numA = float(input("Digite uma valor: "))
#     numB = float(input("Digite outro valor: "))
#     print('A soma dos valore',numA + numB)

# def subtracao():
#     numA = float(input("Digite uma valor: "))
#     numB = float(input("Digite outro valor: "))
#     print('A subtração dos valore',numA - numB)

# def multiplicacao():
#     numA = float(input("Digite uma valor: "))
#     numB = float(input("Digite outro valor: "))
#     print('A multiplicação dos valore',numA * numB)

# def divisao():
#     numA = float(input("Digite uma valor: "))
#     numB = float(input("Digite outro valor: "))
#     print('A a divisão dos valore',numA/numB)

# opcao = 1
# while opcao:
#     print("0. sair")
#     print("1. somar")
#     print("2. subtrair")
#     print("3. Multiplicação")
#     print("4. Divisão")

#     opcao = int(input("Opção: "))
#     if(opcao==1):
#         somar()
#     if(opcao==2):
#         subtracao()
#     if(opcao==3):
#         multiplicacao()
#     if(opcao==4):
#         divisao()
    







# Texto = input("Hello world;")
# print(Texto)



forma = float(input('Escolha uma forma de pagamento? '))
divisao = forma/100
print("Divisão %.2f" %divisao)