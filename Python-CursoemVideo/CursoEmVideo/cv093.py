futebol = {}
gols = []

futebol['jogador'] = input("Nome do jogador: ")
partida = int(input(f"Quantas partidas {'jogador'} jogou: "))

for i in range(partida):
    golsPorPartida = int(input(f"Quantos gols na partida {i+1} ?"))
    gols.append(golsPorPartida)
    futebol['total'] = sum(gols)
print(f"{futebol['jogador']}, gols:{gols}, {futebol['total']}")
