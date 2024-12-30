def calculate_power(base, exponent):
    return base ** exponent

base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))
result = calculate_power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")
