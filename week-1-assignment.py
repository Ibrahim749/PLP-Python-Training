# Basic Calculator Program
# Author: Ibrahim Sawaneh

# Step 1: User input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose an operation (+, -, *, /): ")

# Step 2: Perfoming the Arithmetic Operation based on the User Input

# Addition (+)
if operation == "+":  
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
# Subtraction  (-)  
else:
    if operation == "-": 
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
# Multiplication  (*)      
    else:
        if operation == "*":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
# Division (/)           
        else:
            if operation == "/":
                if num2 != 0:
                    result = num1 / num2
                    print(f"{num1} / {num2} = {result}")
# Error
                else:
                    print("Error: Division by zero is not allowed.")
            else:
                print("Invalid operation. Please choose +, -, *, or /.")
