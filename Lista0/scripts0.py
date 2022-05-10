def main():
  lines = []      #Lista vazia
  largura = ""    # Armazenar a lista de maior quantidade de itens 
  comprimento = -1        # Comprimento dessa lista de maior

  try:            #Corrigindo error
    while True:   #Loop
      lines.append(input()) #adicionando as listas ao lines
  except:
    pass

  for line in lines:        #For para itera os elementos da lista 
    qtd = line.count(',')   #Chamando o metodo count para contar as virgulas da lista   
    if line != '[]':
     qtd += 1

    if(qtd > comprimento):
      largura = line
      comprimento = qtd

    if(largura == comprimento):
      print(line[0])

  print(largura) 

    
if __name__ == '__main__':
    main()
  





