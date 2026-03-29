def main():
    anos = calcular_anos()
    print("Anos necessários:", anos)


def calcular_anos():
    a = 200000
    b = 800000
    anos = 0

    while a <= b:
        a += a * 0.035
        b += b * 0.0135
        anos += 1

    return anos


if __name__ == "__main__":
    main()