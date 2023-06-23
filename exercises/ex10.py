def calculator():
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))
    operation = input("Enter operation (+, *, /, -): ")

    if operation == '+':
        result = num1 + num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    elif operation == '-':
        result = num1 - num2
    else:
        result = "Invalid operation"

    return result


# Test the calculator function
while True:
    result = calculator()
    print(result)
    break
