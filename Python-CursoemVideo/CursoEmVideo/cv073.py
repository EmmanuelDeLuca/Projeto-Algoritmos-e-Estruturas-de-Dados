# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato Brasileiro de futebol, na ordem de colocação.Depois mostre: apenas os 5 primeiros colocados, os ultimos colocados da tabela, uma lista com os time em ordem alfabetica, em que posição na tabela está o sport

times = ('Flamengo', 'Palmeiras', 'CA Mineiro', 'Gremio', 'São Paulo', 'Fluminense', 'Internacional', 'Santos', 'Athtletico Paranaense', 'Corinthians', 'Red Bull', 'Fortaleza', 'Bahia', 'Ceara', 'Cuiaba', 'Atletico Goianiense', 'America Mineiro', 'Juventude', 'Sport', 'Chapecoense')
print(f'Os quatro primeiros lugares: {times[0:4]}')
print(f'Os quatro ultimos times {times[16:]}')
print(f'Por ordem alfabetica: {sorted(times)}')
print(f'Colacação do sport 17 lugar: {times[18]}')