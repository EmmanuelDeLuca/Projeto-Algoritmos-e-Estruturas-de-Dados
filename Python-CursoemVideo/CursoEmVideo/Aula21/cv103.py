from asyncio.windows_events import NULL


def ficha(name = 'Desconhecido', gol = 0):
  print(f"O jogador {name} fez {gol} gol(s) no campeonato")

nome = input("Nome do jogador: ")
gols = input("Numero de gols: ")
if gols.isnumeric():
  gols = int(gols)
else:
  gols = 0

if nome.strip() == '':
  ficha(name = nome)
else:
  ficha(nome, gols)



