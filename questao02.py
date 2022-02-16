import string

continuar = "s"
tamanho = False
digito = False
minusculo = False
maiusculo = False
especial = False

while continuar == "s":
    print(
        "Critérios para uma senha forte:\n"
        " * Possui no mínimo 6 caracteres.\n"
        " * Contém no mínimo 1 digito.\n"
        " * Contém no mínimo 1 letra em minúsculo.\n"
        " * Contém no mínimo 1 letra em maiúsculo.\n"
        " * Contém no mínimo 1 caractere especial. Os caracteres especiais são: !@#$%^&*()-+\n"
    )

    senha = input("Informe a senha: ")
    caracteres = list(senha.strip())
    print(caracteres)


    if len(caracteres) >= 6:
        tamanho = True

    for item in caracteres:
        if item in string.digits:
            digito = True
        if item in string.ascii_lowercase:
            minusculo = True
        if item in string.ascii_uppercase:
            maiusculo = True
        if item in list("!@#$%^&*()-+"):
            especial = True
            # Para adicionar todos os caracteres especiais e pontuação, trocar a list por "string.punctuation"

    if False in [tamanho, digito, minusculo, maiusculo, especial]:
        print("Senha fraca!")
        if tamanho == False:
            print(f"Senha pequena. Acrescente pelo menos mais {6 - len(caracteres)} caracteres.")
        if digito == False:
            print("Adicione ao menos um dígito na senha.")
        if minusculo == False:
            print("Adicione ao menos uma letra minúscula.")
        if maiusculo == False:
            print("Adicione ao menos uma letra maiúscula.")
        if especial == False:
            print("Adicione ao menos um caractere especial.")
    else:
        print("Senha forte!")

    continuar = input("\nGostaria de testar outra senha?(s/n)")
