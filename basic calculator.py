# basic calculator
print("Welcome to Calculator!")

print("\nOperations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1/2/3/4): ")
if(choice=="1" or choice=="2" or choice=="3"  or choice=="4" ):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if (choice == '1'):
        print("Result:", num1 + num2)
    elif( choice == '2'):
        print("Result:", num1 - num2)
    elif (choice == '3'):
        print("Result:", num1 * num2)
    elif( choice == '4'):
        if (num2 == 0):
            print("Cannot divide by zero!")
        else:
            print("Result:", num1 / num2)
else:
    print("Invalid choice!")