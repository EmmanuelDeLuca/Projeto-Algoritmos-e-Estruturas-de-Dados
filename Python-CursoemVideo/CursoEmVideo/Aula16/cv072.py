tuupla = ('zero','um','dois', 'três','quatro','cinco','seis','sete','oito', 'nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito', 'dezenove','vinte')


num = int(input("Digite um numero(0 a 20): "))
while num > 20:
    num = int(input("Tente novamente! Digite um numero(0 a 20): "))
print(tuupla[num])

