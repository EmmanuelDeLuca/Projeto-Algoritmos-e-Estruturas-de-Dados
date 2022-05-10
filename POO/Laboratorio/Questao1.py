
from os import remove


class Menu:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
    self.lista = []

  def cadastrar(self):
    self.lista = []
    self.nome = self.lista.append(self.nome)
    self.idade = self.lista.append(self.idade)

  def procurar(self):
    for i in self.lista:
      if self.lista[i] == self.nome:
        print(f"Pokemon encontrado {i}")
      else:
        print("Pokemon não cadastrado")

  def remover(self):
    for i in self.lista:
      if self.lista[i] == self.nome:
        print(" removido", remove(i))
      else:
        print("Não removido")

  def listaTodos(self):
    for i in self.lista:
      print(f"Todos os pokemons {i}")
      
  def quit(self):
    quit()
  
  

    
  