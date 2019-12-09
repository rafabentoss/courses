n = int(input("digite um número:"))
n1 = 1
n2 = 2
soma = 1

while soma != 0 and n != 0:
    n1 = n % 10
    n = n // 10
    soma = n1 - n2

    n2 = n % 10
    n = n // 10

if soma == 0:
    print("Há números adjacentes iguais.")
else:
    print("Não há números adjacentes iguais")

