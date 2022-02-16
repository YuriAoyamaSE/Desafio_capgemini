continuar = "s"

while continuar == "s":
    print("Desenhar escada de tamanho n.")
    n = int(input("Digite o valor de n: "))

    for degrau in range(1, n+1):
        print(" "*(n-degrau), end="")
        print("*"*degrau)

    continuar = input("\nGostaria de repetir?(s/n)")
