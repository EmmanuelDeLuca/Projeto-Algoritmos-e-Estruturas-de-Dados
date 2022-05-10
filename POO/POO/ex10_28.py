# class Pessoa:
#   def __init__(self, initNome, initIdade, initEndereco):
#     self.nome = initNome
#     self.idade = initIdade
#     self.endereco = initEndereco

# p1 = Pessoa("david", 23, "Rua adolfo caminha")
# p2 = Pessoa("Elida", 25, "Igarassu")

# print(p1.nome)

# Modificando mais ainda o condigo


# class Pessoa:
#   def __init__(self, initNome, initIdade, initEndereco):
#     self.nome = initNome
#     self.idade = initIdade
#     self.endereco = initEndereco

#   def imprimeDados(self):
#     print(self.nome, self.idade, self.endereco)
  
#   def fazAniversario(self):
#     self.idade += 1
  
#   def atualizarEndereco(self, novoEndereco):
#       self.endereco = novoEndereco

#   def retornaAnoNascimento(self):
#     return 2022-self.idade


# def moraMesmoEndereco(pessoa1, pessoa2):
#   if(pessoa1.endereco != pessoa2.endereco):
#     return True
#   else:
#     return False

# p1 = Pessoa("david", 23, "Rua adolfo caminha")
# p2 = Pessoa("Elida", 25, "Igarassu")


# print(moraMesmoEndereco( p1, p2))


#========== Melhores praticas ===========#
# ###################################### #

#Ao inves de fazer como foi anteriomente, é so fazer uma função get

#Pior pratica
# print(p1.nome)
# print(p2.nome)

#Boa pratica
#Cria uma função chamda getNome
# def getNome(self):
  # return self.nome


# print(p1.getNome())
# print(p2.getNome)


#Boa pratica para atualização


# def setNome(self, novoNome):
  # self.nome = novoNome

# p1.setNome("Joao")

#Má pratica
# p1.nome = "Joao


#Get: pegar
#set: Atualizar

#Protocolo de mudança

class Conta:
  def __init__(self, initCPF, initValorInicial):
    self.cpf = initCPF
    self.saldo = initValorInicial
    self.taxaSaque = 0.25

  def fazerSaque(self, valor):
    self.saldo -= valor + self.taxaSaque
  
  def retornaSaldo(self):
    return self.saldo

#Herança POO

class Poupanca(Conta):
  def __init__(self, initCPF, initValorInicial):
    super().__init__(initCPF, initValorInicial)


conta1 = Conta("111-222-333-4", 100)
conta1.fazerSaque(40)

contaPoupanca1 = Poupanca("333-444-555-6", 400)
contaPoupanca1.fazerSaque(100)

print(conta1.retornaSaldo())
print(contaPoupanca1.retornaSaldo())