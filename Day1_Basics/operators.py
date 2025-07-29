#ARITHMATIC OPERATORS
a=15
b=4
print("Addition:", a + b)  
print("Subtraction:", a - b)  
print("Multiplication:", a * b)  
print("Division:", a / b)  
print("Floor Division:", a // b)  
print("Modulus:", a % b)  
print("Exponentiation:", a ** b)  

#LOGICAL OPERATORS
x = True
y = False
print("Logical AND:", x and y) 

print("Logical OR:", x or y)  

print("Logical NOT:", not x)  

#COMPARISON OPERATORS
a = 10
b = 20
print("Equal to:", a == b) 
print("Not equal to:", a != b)  
print("Greater than:", a > b)  
print("Less than:", a < b)  
print("Greater than or equal to:", a >= b)  
print("Less than or equal to:", a <= b)  

'''
#BITWISE OPERATORS
x = 5  # Binary: 0101
y = 3  # Binary: 0011
print("Bitwise AND:", x & y)  # This will print 1 (Binary: 0001)
print("Bitwise OR:", x | y)  # This will print 7 (Binary: 0111)
print("Bitwise XOR:", x ^ y)  # This will print 6 (Binary: 0110)
print("Bitwise NOT:", ~x)  # This will print -6 (Binary: 1010 in two's complement)
print("Left Shift:", x << 1)  # This will print 10 (Binary: 1010)
print("Right Shift:", x >> 1)  # This will print 2 (Binary: 0010)
'''

#ASSIGNMENT OPERATORS
x = 10
x += 5  
print("After += :", x) 
x -= 3  
print("After -= :", x)  
x *= 2  
print("After *= :", x)  
x /= 4  
print("After /= :", x)  
x //= 2  
print("After //= :", x)  
x %= 2  
print("After %= :", x)  
x **= 3 
print("After **= :", x)  

#IDENTITY OPERATORS
a = [1, 2, 3]
b = a
c = a[:]
print("a is b:", a is b)  
print("a is c:", a is c)  
print("a is not c:", a is not c) 

