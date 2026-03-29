def main():
    a1 = float(input("Primeiro termo: "))
    r = float(input("Razão: "))
    n = int(input("Quantidade de termos: "))

    gerar_pg(a1, r, n)


def gerar_pg(a1, r, n):
    i = 1
    termo = a1

    while i <= n:
        print(termo)
        termo *= r
        i += 1


if __name__ == "__main__":
    main()