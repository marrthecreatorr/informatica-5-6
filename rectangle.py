def main():

    l = 5
    w = int(input("Width: "))
    print("o" * w)
    print("o" * w)
    print("o" * w)
    print("o" * w)
    print("o" * w)

    p = (2 * l) + (2 * w)
    print("perimeter:", p)

    a = (l * w)
    print("Area", a)

    d = ((1**2) + (w**2) )**0.5
    print("Diagonal:" , d)


if __name__ == "__main__":
    main()

