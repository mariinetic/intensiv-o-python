# Solicitar as coord ao usuário
cont_coord = int(input("quantos pares de coordenada você ira inserir? "))
coord = [(float(input(f"Digite a coordenada para ser X{i+1}: ")), float(input(f"Digite a coordenada para se Y{i+1}: "))) for i in range(cont_coord)]

# Gerar e imprimir todos os conjuntos possíveis de coord
print("\nEsses são todos as póssiveis junção dessas coordenadas!")
for i in range(len(coord)):
    for j in range(i + 1, len(coord)):
        print([coord[i], coord[j]])
2
