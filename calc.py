# create functions for the calculations
# create a function to add two numbers
def add(x, y):
    return x + y

# create a function to subtract two numbers
def subtract(x, y):
    return x - y

# create a function to multiply two numbers
def multiply(x, y):
    return x * y

# create a function to divide two numbers
def divide(x, y):
    return x / y

print("Select your required operation: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# get input from the user
while True:
    option = input("Select option 1/2/3/4: ")

# check if choice is one of the four options
    if option in ("1", "2", "3", "4"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please pick another option.")
            continue

        if option == "1":
            print(num1, "+", num2, "=", add(num1, num2))

        elif option == "2":
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif option == "3":
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif option == "4":
            print(num1, "/", num2, "=", divide(num1, num2))

# check if the user wants another calculation
# break the while loop if the answer is no
        
        next_calculation = input("Do you want to do another calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")
