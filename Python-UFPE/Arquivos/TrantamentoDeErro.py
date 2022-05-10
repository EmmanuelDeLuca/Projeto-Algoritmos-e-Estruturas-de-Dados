# Tratamento de error
# 10 * (1/0)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
# >>> 4 + spam*3
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'spam' is not defined
# >>> '2' + 2
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: Can't convert 'int' object to str implicitly

fim = False
while not fim:
    try:
        valor = int(input("Digite um valor positvo e inteiro: "))
        while valor <= 0:
            valor = int(input("Valor invalido. Digite um valor positivo e inteiro: "))
            
    except ValueError:
        print("Erro. O valor digitado deve ser um numero inteiro")
    else:
        fim = True

# Error ao ler o nome em arquivo 
frag = False
while not  frag:
    try:
        nome = input("Digite o nome do arquivo: ")
        arq = open(nome, 'r')
        for linha in arq:
            print(linha)
        arq.close()
    except FileNotFoundError:
        print("ERRO. Digite um caminho certo")
    else:
        print("Programa finalizado com sucesso.")
        frag = True
    