def pattern_two():
    n = int(input("Enter the number of rows: "))
    for i in range(1, n + 1):
        print(str(i) * (n - i + 1))

pattern_two()
