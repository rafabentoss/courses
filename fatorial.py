n = int(input("Digite o valor de n: "))
fatorial = i = 1

while n >= i:
    fatorial = fatorial * i
    i = i + 1
if n < i:
    print (fatorial)
