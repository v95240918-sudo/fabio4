def main():
    aprovados, reprovados, total = processar_alunos()

    print("Aprovados:", aprovados)
    print("Reprovados:", reprovados)
    print("Total de alunos:", total)


def processar_alunos():
    aprovados = 0
    reprovados = 0
    total = 0

    matricula = int(input("Matrícula (0 para sair): "))

    while matricula != 0:
        n1 = float(input("Nota 1: "))
        n2 = float(input("Nota 2: "))
        n3 = float(input("Nota 3: "))

        media = (2*n1 + 3*n2 + 5*n3) / 10

        if media >= 7:
            aprovados += 1
        else:
            reprovados += 1

        total += 1
        matricula = int(input("Matrícula (0 para sair): "))

    return aprovados, reprovados, total


if __name__ == "__main__":
    main()