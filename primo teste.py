    # leia o valor de n
n = int(input(print "Digite o valor de n (n > 0): "))

é_primo = True

    # procure por um divisor de n entre 2 e n-1
divisor = n - 1
    while divisor < n and é_primo:  # equivalente a "div... and é_primo == True:"
        if n % divisor == 0:
            é_primo = False
        divisor -= 1

        if é_primo and n != 1:  # 1 não é primo
        print(n, "é primo")
    else:
        print(n, "não é primo")
