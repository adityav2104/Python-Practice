#BASIC FUNCTION DECLARATION
def add(a, b):
    return a + b
s = add(5, 3)
print("Sum:", s)

#FUNCTION WITHIN A FUNCTION
def multiply(a, b):
    return a * b
def calculate(a, b):
    product_result = multiply(a, b)
    return product_result
result = calculate(4, 5)
print("Product:", result)

#ANONYMOUS FUNCTION
multiply = lambda a, b: a * b
result = multiply(6, 7)
print("Anonymous Function Result:", result)