s = 0   
numerador = 1
denominador = 1
while numerador <= 100:
    s+=numerador/denominador
    numerador+=2
    denominador+=1
    
    
print(f"S = {s}")

S = 0
denominador = 1
for numerador in range(1, 100, 2):
    S += numerador/denominador
    denominador += 1

print("S =", S)