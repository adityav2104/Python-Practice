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

#SELF AS THE FIRST ARGUMENT
class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def subtract(self):
        return self.a - self.b
calc = calculator(10, 5)
print("Class Method Add:", calc.add())
print("Class Method Subtract:", calc.subtract())    

