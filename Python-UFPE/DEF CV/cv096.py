# Faça um programa que tenha uma função chamada área(), que receba
# as dimensoes de um terreno retangular(largura e comprimento) e mostre a area do terreno.

def area(largura, comprimeto): #Aqui criamos a função e passamos os paramentos
    areaDoTerreno = largura * comprimeto #variavel para calcular a area
    print(f'A area de um terreno {largura}x{comprimeto} é de {areaDoTerreno}m')

area(float(input("LARGURA (M): ")),float(input("COMPRIMENTO (M): "))) #Passando os paramentos 
