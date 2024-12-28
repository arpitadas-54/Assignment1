def calculate_interest():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest (in %): "))
    time = float(input("Enter the time period (in years): "))
    
    simple_interest = (principal * rate * time) / 100
    print(f"Simple Interest: {simple_interest}")
    
    compound_interest = principal * ((1 + rate / 100) ** time - 1)
    print(f"Compound Interest: {compound_interest}")

calculate_interest()
