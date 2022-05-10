def maior(*num):
  lista = []
  tam = len(num)
  print("Analisando os valores passados...")
  print(f'{num} Foram informados {tam} valores ao todo')
  for i in num:
    lista.append(i)
  print('O maior valor informado foi',max(lista))
    
    

maior(1000,1000000,10000000000,1000000000000000)