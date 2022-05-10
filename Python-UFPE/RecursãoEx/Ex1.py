# SubRotina
def mergulho_i(n, prof = 0):
	for i in range (3):
		print(f"{prof} Metros.")
		n = n - 1
		prof = prof + 1
	return

# RECURSÃO
def mergulhar(n, metros = 0):
    if n < 1:
        return
    else:
        print(f"{metros} Metros.")
        mergulhar(n - 1, metros + 1)
mergulhar(5)


