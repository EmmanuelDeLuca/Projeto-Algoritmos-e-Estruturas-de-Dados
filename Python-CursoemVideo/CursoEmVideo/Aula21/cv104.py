def leiaInt(num):
  while True:
    n = str(input(num))
    if n.isnumeric():
      print(f"Você acabou de digitar o numero {n}")
      break
    else:
      print("ERRO! digite um valor valido")
      
    
n = leiaInt("Digite um numero: ")
