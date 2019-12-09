

n = int(input("Digite o valor de n", ))
k = int(input("Digite o valor de k", ))

def fatorial(x):
    fat = i = 1
    while x >= i:
        fat = fat * i
        i = i + 1
    return fat

binomial = fatorial(n) / (fatorial(k) * fatorial(n - k))
print(binomial)