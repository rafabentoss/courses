N = int(input("Digite o número:") )
soma = 0

while N >= 1:
    digito = N % 10
    N = N // 10
    soma = digito + soma
print("A soma dos dígitos é", soma)