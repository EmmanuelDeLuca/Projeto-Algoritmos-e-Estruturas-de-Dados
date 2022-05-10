def contador(inicio,fim,passo):
  if inicio < fim:
    for c in range(inicio,fim, passo):
      print(c)
  else:
    cont = inicio
    while cont >= fim:
      print(f'{cont} ', end='')
      cont -= passo
    



inicio = int(input("Inicio: "))
fim = int(input("Fim: ")) + 1
passo = int(input("Passo: "))
contador(inicio,fim, passo)