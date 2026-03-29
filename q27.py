def main():
    analisar_pessoas()


def analisar_pessoas():
    total = 0
    soma_idade_h = 0
    soma_idade_m = 0
    qtd_h = 0
    qtd_m = 0
    homens_solteiros = 0
    mulheres_solteiras = 0
    mulheres_div_30 = 0

    i = 1
    while i <= 100:
        sexo = int(input("Sexo (1-M,2-F): "))
        idade = int(input("Idade: "))
        estado = int(input("Estado civil (1-4): "))

        if sexo == 1:
            soma_idade_h += idade
            qtd_h += 1
            if estado == 2:
                homens_solteiros += 1
        else:
            soma_idade_m += idade
            qtd_m += 1
            if estado == 2:
                mulheres_solteiras += 1
            if estado == 3 and idade > 30:
                mulheres_div_30 += 1

        total += 1
        i += 1

    if qtd_h > 0:
        print("Média idade homens:", soma_idade_h / qtd_h)

    if qtd_m > 0:
        print("Média idade mulheres:", soma_idade_m / qtd_m)

    print("Homens solteiros %:", homens_solteiros * 100 / total)
    print("Mulheres solteiras %:", mulheres_solteiras * 100 / total)
    print("Mulheres divorciadas >30:", mulheres_div_30)


if __name__ == "__main__":
    main()