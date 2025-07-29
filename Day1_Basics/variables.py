#DYNAMIC TYPING
x= 10
print(type(x))  

x = 10.5
print(type(x))  

x = "Hello"
print(type(x)) 


#ASSIGNING DIFF VALUES
x = y = z = 5
print(x,y,z)  


#DELETING A KEYWORD USING DEL
x = 10
print(x)  
del x
print(x)  

#SWAPPING VALUES
a = 5
b = 10
print("Before swapping:", a, b)  
a, b = b, a
print("After swapping:", a, b)  

#COUNTING CHARACTERS IN A STRING
string = "Hello World"
length = len(string)
print("Length of the string:", length)  