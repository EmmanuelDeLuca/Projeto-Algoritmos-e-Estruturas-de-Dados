class Pokemon:
    def __init__(self, nomeInit, idadeInit):
        self.nome = nomeInit
        self.idade = idadeInit

def imprimaMenu():
    print("1 - Inserir Pokemon")
    print("2 - Procurar pelo nome")
    print("3 - Remover pelo nome")
    print("4 - Imprimir todos")
    print("5 - Encerrar o programa")

continuaPrograma = True
listaPokemons = []
while continuaPrograma:
    imprimaMenu()
    opcao = int(input("Digite a opcao: "))

    if opcao == 1:
        nome = input("Digite o nome: ")
        idade = input("Digite a idade")
        pokemon = Pokemon(nome, idade)
        listaPokemons.append(pokemon)

    elif opcao == 2:
        nome = input("Digite o nome: ")
        encontrado = False
        for pokemon in listaPokemons:
            if pokemon.nome == nome:
                print("Pokemon localizado")
                encontrado = True
        if not encontrado:
            print("Pokemon não encontrado")

    elif opcao == 3:
        nome = input("Digite o nome: ")
        encontrado = False
        contador = 0
        while (contador < len(listaPokemons) and not encontrado):
            if listaPokemons[contador].nome == nome:
                print("Pokemon localizado e excluido")
                listaPokemons.remove(listaPokemons[contador])
                encontrado = True
            contador+=1
    elif opcao == 4:
        for pokemon in listaPokemons:
            print(pokemon.nome)
    
    elif opcao == 5:
        print("Programa finalizado")
        continuaPrograma = False
    else:
        print("Opção não existente")