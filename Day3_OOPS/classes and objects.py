# BASIC STRUCTURE OF CLASS
'''
class student:
    def __init__(self, name, age,marks):
        self.name = name
        self.age = age
        self.marks = marks


    def showdata(self):
         print(f"Your name is : {self.name} \n Your age is : {self.age} \n Your Makrs are : {self.marks}")

s = student("Aditya", 23, 50)
s.showdata()
#print(s.name)



#CLASS ATTRIBUTE

class dog:
    count = 0; 
    
    def increase(self):
        dog.count += 1

d = dog()
d.increase()
print(d.count)

d1 = dog()
d1.increase()
print(d1.count)

print(dog.count)

'''



class teacher:
    def __init__(self, name, id, marks):
        self.name = name
        self.id = id
        self.marks = marks

    def display(self):
        print(f"Your name : {self.name} \n Your ID : {self.id} \n Your marks : {self.marks}")

class student(teacher):
    
              