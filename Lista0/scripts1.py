def main():
  chaves = input()
  pilha = []
  
  

  for expre in chaves:
    if chaves == '{':
      pilha.append('{')
    if chaves == '}':
      if len(pilha) > 0:
        pilha.pop()
      else:
        pilha.append('}')
        break

  if len(pilha) == 0:
    print('S')
  else:
    print('N')

if __name__ == '__main__':
    main()
