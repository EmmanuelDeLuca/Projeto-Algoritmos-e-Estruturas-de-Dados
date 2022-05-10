import datetime

def voto(ano=0):
  currentDateTime = datetime.datetime.now()
  date = currentDateTime.date()
  year = date.strftime("%Y")
  eleiçao = int(year) - ano
  
  if eleiçao < 16:
    print(f"Sua idade é {eleiçao}. Voto Negado!")
  elif(eleiçao == 16):
    print(f"Sua idade é {eleiçao}. Voto Opcional!")
  else:
    print(f"Sua idade é {eleiçao}. Voto Obrigatorio!")


ano = int(input("Digite seu ano: "))
voto(ano)

