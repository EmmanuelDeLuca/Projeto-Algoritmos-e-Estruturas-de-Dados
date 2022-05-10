def mediana(vetor1, vetor2, n, m) :
	i = 0 #indice atual do entrada do veto1
	j = 0  #o mesmo para 2
	m1, m2 = -1, -1
	if((m + n) % 2 == 1) :
		for count in range(((n + m) // 2) + 1) :
			if(i != n and j != m) :		
				if vetor1[i] > vetor2[j] :
					m1 = vetor2[j]
					j += 1
				else :
					m1 = vetor1[i]
					i += 1		
			elif(i < n) :		
				m1 = vetor1[i]
				i += 1
			else :		
				m1 = vetor2[j]
				j += 1	
		return m1
	else :
		for count in range(((n + m) // 2) + 1) :		
			m2 = m1
			if(i != n and j != m) :	
				if vetor1[i] > vetor2[j] :
					m1 = vetor2[j]
					j += 1
				else :
					m1 = vetor1[i]
					i += 1		
			elif(i < n) :		
				m1 = vetor1[i]
				i += 1
			else :		
				m1 = vetor2[j]
				j += 1	
		return (m1 + m2)/2
if __name__ == "__main__":
    arr1 = []
    entrada = input().split()
    for i in entrada:
        arr1.append(int(i))
    arr2= []
    entrad = input().split()
    for i in entrad:
        arr2.append(int(i))
n1 = len(arr1)
n2 = len(arr2)
print('%.2f'%mediana(arr1, arr2, n1, n2))