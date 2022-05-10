qtdeInstrucoes = []

ns = [10, 20, 30, 40, 50 , 60]

for N in ns:
  contInstrucao = 0
  vetor1 = range(N)
  vetor2 = range(N)

  encontrou = False
  contInstrucao += 1
  for i in range(N):
    contInstrucao += 1
    for j in range(N):
      contInstrucao += 1
      contInstrucao += 1
      if(vetor1[i] == vetor2[j]):
        encontrou = True
    contInstrucao += 1
  contInstrucao += 1
  qtdeInstrucoes.append(contInstrucao)

print(qtdeInstrucoes)