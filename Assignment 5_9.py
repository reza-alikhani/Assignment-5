def multiplication_chart(m, n):
    print("   ", end="")
    for column in range(1, n + 1):
        print(f"{column:4}", end="")
    print("\n")

    for row in range(1, m + 1):
        print(f"{row:2} |", end="")
        for column in range(1, n + 1):
            print(f"{row * column:4}", end="")
        print()

m = int(input("Enter number of rows (m): "))
n = int(input("Enter number of columns (n): "))

multiplication_chart(m, n)
