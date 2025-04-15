first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")
operator = input("Enter the operator (+, -, *, /): ")
if operator == "+":
    result = float(first_number) + float(second_number)
    print(f"Result: {result}")
elif operator == "-":
    result = float(first_number) - float(second_number)
    print(f"Result: {result}")
elif operator == "*":
    result = float(first_number) * float(second_number)
    print(f"Result: {result}")
elif operator == "/":
    result = float(first_number) / float(second_number)
    print(f"Result: {result}")
else:
    print("Invalid operator. Please use +, -, *, or /.")
