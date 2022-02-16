continuar = "s"

while continuar == "s":
    print("Procurar número de pares de substrings que são anagramas.")
    palavra = input("Digite a palavra desejada: ").strip()
    caracteres = list(palavra)
    substrings = []
    lista_comparativa= []
    anagramas = []

    for final in range(1, len(caracteres)+1):
        for inicio in range(0, final):
            substrings.append(palavra[inicio:final])

    for posicao1 in range(0, len(substrings)-1):
        item1 = substrings[posicao1]
        lista1 = list(item1)
        lista1.sort()

        for posicao2 in range(posicao1+1, len(substrings)):
            item2 = substrings[posicao2]
            lista2 = list(item2)
            lista2.sort()
            if len(lista1) == len(lista2) and lista1 == lista2:
                anagramas.append([item1, item2])

    print("Palavra: ", palavra)
    print("Conjunto dos anagramas pares: ", anagramas)
    print("\nTotal de pares que são anagramas: ", len(anagramas))

    continuar = input("\n Deseja fazer outro teste? (s/n) ")
