#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parametro e mostre uma mensagem com tamanho adaptável.
def escreva(texto):
    tam = len(texto)
    print('-'*tam)
    print(texto)
    print('-'*tam)
escreva(input('Digite um texto qualquer: '))