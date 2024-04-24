def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            if c != 1:
                print(c, end=' x ')
            else:
                print(c, end=' = ')
    return f
numero = int(input("Digite seu número para calcular o fatorial: "))
print(fatorial(numero, True))