nome = input("Digite o nome da sua cidade: ")
frase = nome.split()
cidade = frase[(0)]
cidade1 = 'SANTO' in cidade

if cidade1:
    print("Comaça com SANTO")
else:
    print('não começa')

