print("Here is the calculator you need!")
x,y = input("Enter two numbers separated by space: ").split()
x = float(x)
y = float(y)
print("\n\nEnter the operation you want to perform: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus\n6. Exponentiation")
operation = int(input("Enter the operation number: "))
if operation == 1:
    print(f"The result of addition is: {x + y}")
elif operation == 2:    
    print(f"The result of subtraction is: {x - y}")
elif operation == 3:    
    print(f"The result of multiplication is: {x * y}")
elif operation == 4:    
    print(f"The result of division is: {x / y}")
elif operation == 5:    
    print(f"The result of modulus is: {x % y}")
elif operation == 6:    
    print(f"The result of exponentiation is: {x ** y}")
else:
    print("Invalid operation selected. Please try again.")
print("\n\nThank you for using the calculator!")