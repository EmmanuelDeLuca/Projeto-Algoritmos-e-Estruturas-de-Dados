# Considerando que um Uber só pode rodar se seu modelo for a partir de 2009, mostre para cada modelo (no terminal mesmo):
# MODELO_X - ANO_X pode rodar de uber.
# No final mostre a média dos anos.
# Mas nem todos vão poder rodar, então grave em um NOVO ARQUIVO os carros que não podem, neste formato:
# MODELO_X - ANO_X NÃO pode rodar de uber.
# OBS: Pergunte ao usuário o nome do novo arquivo
frag = False
while not frag:
    try:
        
        nome = input("Digite o nome do arquivo: ")
        arq_uber = open(nome, 'r')
        arq_antigoUber = open('modeloVelhoUber.txt', 'w')
        media = 0.0
        motoristas = 0

        with arq_uber, arq_antigoUber:
            for mod in arq_uber:
                placa, ano, modelo = mod.split()

                if int(ano) >= 2009:
                    motoristas += 1
                    media += int(ano)
                    total = media/motoristas
                    print(f"Motorista permitido! {modelo} - {ano}")
                else:
                    print(f"Motorista Negago! {modelo} - {ano}")
                    arq_antigoUber.write(f'{placa} {ano} {modelo}\n')
    except FileNotFoundError:
        print("Caminho do arquivo Errado")
    else:
        frag = True
        print(f"Media dos anos dos motoristas: {total}")
