def maior_primo (n)

n = int(input( "Digite o valor de n (n > 0): "))

def éPrimo(k)
    primo = True

    # procure por um divisor de n entre 2 e n-1
    divisor = 2
    while divisor < n and primo:
        if n % divisor == 0:
            primo = False
        divisor = divisor + 1

    if primo and n != 1:  # 1 não é primo
            print(n, "é primo")
    else:
            print(n, "não é primo")
