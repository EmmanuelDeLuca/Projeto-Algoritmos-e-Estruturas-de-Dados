user = int(input("Qual a distancia da sua viagem :"))
if user <= 200:
    x = (user * 0.50)
    print("Sua passagem irá custar %d reais" %x)
else:
    y = user * 0.45
    print("Sua passsagem irá custar %d reais" %y)