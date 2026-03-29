def main():
    processar_pesquisa()


def processar_pesquisa():
    soma_idade_otimo = 0
    qtd_otimo = 0
    qtd_regular = 0
    qtd_bom = 0
    total = 0

    idade = int(input("Idade (-1 para sair): "))

    while idade != -1:
        opiniao = int(input("Opinião (1-4): "))

        if opiniao == 1:
            soma_idade_otimo += idade
            qtd_otimo += 1
        elif opiniao == 2:
            qtd_bom += 1
        elif opiniao == 3:
            qtd_regular += 1

        total += 1
        idade = int(input("Idade (-1 para sair): "))

    if qtd_otimo > 0:
        print("Média idade ótimo:", soma_idade_otimo / qtd_otimo)

    print("Qtd regular:", qtd_regular)

    if total > 0:
        print("Percentual bom:", qtd_bom * 100 / total, "%")


if __name__ == "__main__":
    main()