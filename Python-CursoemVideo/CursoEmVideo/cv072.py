tuupla = ('zero','um','dois', 'três','quatro','cinco','seis','sete','oito', 'nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito', 'dezenove','vinte')

usuario = int(input("Digite um numero (entre 0 e 20):" ))
while (usuario < 0) and (usuario > 20):
    usuario = int(input("Error. Digite um numero (entre 0 e 20):" ))
print(f'você digitou: {tuupla[usuario]}')



