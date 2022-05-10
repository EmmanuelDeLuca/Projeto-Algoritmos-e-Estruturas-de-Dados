velocidade = int(input("Digite sua velocidade"))

if velocidade > 80:

    print("Velocidade acima de 80km/h -> Multa")
    print("Multado!")

    x = (velocidade - 80)*7

    print(f'Sua multa irá custar:{x} ')

else:
    print('Dentro do limite permitido')