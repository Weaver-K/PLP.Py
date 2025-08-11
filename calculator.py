# Asks user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
calculation = input("Enter an operation (+, -, *, /): ")

# Perform calculation
if calculation == '+':
    result = num1 + num2
elif calculation == '-':
    result = num1 - num2
elif calculation == '*':
    result = num1 * num2
elif calculation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid calculation"

print("Result:", result)