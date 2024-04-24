def conjunto_de_partes(conjunto):
    partes = [[]]
    for elemento in conjunto:
        partes.extend([subset + [elemento] for subset in partes])
    return partes
elementos = input("Para facilitar por favor digite os numeros do conjunto com espaço!: ").split()
print("\nAbaixo estão todas as combinações possíveis levando com consideração a regra do 2 elevado a n sendo n o numero de complementos do conjunto:")
for conjunto in conjunto_de_partes(elementos):
    print(conjunto)
