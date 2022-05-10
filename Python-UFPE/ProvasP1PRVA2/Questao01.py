# – A média ponderada de N números é a soma dos produtos de cada um deles multiplicados
# por seus respectivos pesos; o resultado dessa soma é então dividido pela soma dos pesos.
#  A média ponderada é utilizada em diversas disciplinas para calcular os resultados dos alunos
# considerando duas avaliações parciais com pesos variáveis. As regras para definição do
# resultado são as seguintes:
# • Se a média do aluno for maior ou igual a sete, o aluno “está aprovado”.
# • Se a média do aluno for menor que três, o aluno “está reprovado”.
# • Se a média do aluno for menor que sete e maior ou igual a três, ele “fará prova final”.

# Faça uma subrotina Python do tipo procedimento que (a) receba o nome de um único aluno
# como parâmetro, (b) leia as notas das duas avaliações parciais desse aluno, (c) calcule sua média,
# e (d) imprima seu resultado como: "O aluno __________ obteve média ____ e __________."
# OBS - Os pesos utilizados no procedimento (peso1 e peso2) são parâmetros opcionalmente
# recebidos na chamada e, se não forem informados, seus valores devem ser 1.
# OBS2 - Você pode (ou não) incluir um programa principal para testar a sua subrotina: somente a
# função será avaliada na correção.
# N * P + N2 * P2/p+p2

def MediaDeAluno(num, nota1, nota2, peso1, peso2):
    media = ((nota1 * peso1) + (nota2 * peso2)) / peso1+peso2
    if peso1 and peso2 == 0:
        return 1 
    else:
        if media >= 7:
            print(f"O aluno{num} obteve média {media} e Aprovado")
        elif media <= 3:
            print(f"O aluno{num} obteve média {media} e Reprovado")
        else:
            print(f"O aluno{num} obteve média {media} e irá pra Final")

    return media
nome = input("Diga seu nome: ")
nota1 = float(input("Diga suas notas: "))
nota2 = float(input("Diga suas notas: "))
peso1 = float(input("Digige seu peso: "))
peso2 = float(input("Digite seu peso: "))

pond = MediaDeAluno(nome, nota1, nota2, peso1, peso2)
print(pond)
