# Fibonacci Series
def fibonacci_series():
    n = int(input("Enter the number of terms: "))
    a, b = 0, 1
    print("Fibonacci Series:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

fibonacci_series()
