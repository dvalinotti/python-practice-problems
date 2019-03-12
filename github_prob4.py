# Define a class that has at least two methods: getString and printString

class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def getSring(self):
        return (self.name + ", age " + str(self.age))
    def printString(self):
        print (self.name + ", age " + str(self.age))
        
p = Person('Dan', 22)
print(p.getSring())
p.printString()