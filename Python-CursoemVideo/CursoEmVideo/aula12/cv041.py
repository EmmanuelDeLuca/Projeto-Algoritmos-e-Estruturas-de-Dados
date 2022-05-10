
# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# – Até 9 anos: MIRIM

# – Até 14 anos: INFANTIL

# – Até 19 anos: JÚNIOR

# – Até 25 anos: SÊNIOR

# – Acima de 25 anos: MASTER
ano = int(input('Digite seu ano de nascimento: '))
idade = 2021 - ano
if idade <= 9:
    print("Mirin")
elif(idade > 9 and idade <= 14):
    print('Infantil')
elif(idade > 14 and idade <= 19):
    print('Junior')
elif(idade > 19 and idade <= 20):
    print('Senior')
else:
    print('Master')