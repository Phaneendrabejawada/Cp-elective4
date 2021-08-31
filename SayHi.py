# Write a class called Dog that has two properties: name and age. Write a constructor that takes three arguments self, name and age and set these to the object properties.
# Now write a function sayHI(dog) where dog is the dog class object that returns a Hi, my name is <dog’s name> and I am <age> years old!

# sayHi(d1) # Hi, my name is Dot and I am 4 years old!
# sayHi(d2) # Hi, my name is Elf and I am 3 years old!

class Dog(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        


def SayHi(dog):
    print(f'Hi, my name is {dog.name} and I am {dog.age} years old!')
        
    
first=Dog('Tarly',12)
second=Dog('Madaly',5)
SayHi(first)
SayHi(second)
