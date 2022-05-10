from asyncio.windows_events import NULL


class Aluno:
  def __init__(self, nome, cpf):
    self.nome = nome
    self.cpf = cpf
    
  
  def inicializarNota(self, nota, numeroDeprova):
    
    self.nota = nota
    self.numeroDeprova = numeroDeprova

  
  def verificaSituacaoMedia(self):
    media = sum(self.nota)/ self.numeroDeprova
    if media >= 7:
      print(True)
    else:
      print(False)

  def imprimirInformaçoes(self):
    if self.nota and self.numeroDeprova == NULL:
      print(self.nome, self.cpf)
    else:
      print(self.nome, self.cpf, self.nota, self.numeroDeprova)
    
p1 = Aluno('David', '111-222-333-44')
p1.inicializarNota([10,10,10,10], 4)
p1.verificaSituacaoMedia()
p1.imprimirInformaçoes()




