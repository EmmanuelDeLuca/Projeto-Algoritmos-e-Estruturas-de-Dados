# def mostraLinha():
#   print("---------------------------------------")
# mostraLinha()
# print("           SISTEMA DE ALUNOS           ")
# mostraLinha()

# Recebendo parametro

# def mensagem(msg):
#   print("-"*30)
#   print(msg)
#   print("-"*30)
# mensagem("Sistema de Alunos")

# -----Parte pratica da aula------#

# def soma(a, b):
#   s = a + b
#   print(s)

# soma(4,5)
# soma(8, 9)
# soma(2, 1)
# soma(4,1)

# def soma(a, b):
#   print(f'A={a} e B ={b}')
#   s = a + b
#   print(f'A soma A + B = {s}')
# soma(2,1)

# Enpacotar parametros
# * -> tira do enpacotamento
# def contador(*num):
#   for valor in num:
#     print(valor, end='')
#   print("fim")
# contador(5,7,3,1,4)

# def contado(*num):
#   tam = len(num)
#   print(f'Recebi os valores {num} e sao ao todo {tam} numero')

# contado(2,1,7)
# contado(8,0)
# contado(4,4,7,6,2)

# def dobra(lst):
#   pos = 0
#   while pos < len(lst):
#     lst[pos]*=2

# valores = [6,3,2,1]
# dobra(valores)
# print(valores)

# def soma(* valores):
#   s = 0
#   for num in valores:
#     s+= num
#   print(f'soma valores {valores}temos {s}')


# soma(5,2)

# def calcu(num):
#   if num == 1:
#     a = float(Input("Digite o primeiro valor: "))

# Docstring




# def contador(i,f,p):

#   c = i
#   while c <= f:
#     print(f'{c}', end='..')
#     c+=p
#   print("FIM")


# contador(2,10,2)

# def somar(a = 0, b = 0, c = 0):
#   s = a + b + c
#   print(f'soma dos valores : {s}')

# somar(8,4)

# Escopo de variavel
# def teste():
#   print(f'na função teste, n vale{n}')
# n = 2
# print(f"No program principal, n vale {n}")

# Fatorial

# Fatorial com for
# def fatorial(num=1):
#   fat = 1
#   for i in range(num, 0, -1):
#     fat*=i
#   return fat

# n = (int(input("Digite o valor ")))
# print(fatorial(n))

# Fatorial com while

# def fatorial(n=1):
#   fat = 1
#   while n > 1:
#     fat*=n
#     n-=1
#   return fat

# n = int(input("Digite o numero: "))
# print(fatorial(n))


# def calculadora(num=0, a = 0, b = 0):
  
#   s = a + b
#   print(s)
  

# print("1.Somar\n2.Divisão\n3.Subtração\n4.Multiplicação")
# n = (int(input("Escolha a operação: ")),int(input("Escolha o primeiro: ")),int(input("Escolha o segundo: ")))
# print(calculadora(n))
