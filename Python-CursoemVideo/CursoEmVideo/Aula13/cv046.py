import time

for i in range(10, -1, -1):
    time.sleep(1)
    print(i)
    if i == 0:
        print("Feliz Ano novo")
