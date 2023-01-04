mydict = { 'a':304, 'e':53, 'g':1000, 'h':100 , 'f': 200}
counter = 0
dict = []
for i in mydict:
    if mydict[i] > counter:
        counter = mydict[i]
        if counter == mydict[i] :
            dict.append(i)

#print(dict)
mydict = { 'a':304, 'e':53, 'g':1000, 'h':100 , 'f': 200}
maxkey = max(mydict, key = mydict.get)
#print(maxkey)

# Concept of class
class Car:

    def __init__(self,modelname,year):
        self.modelname = modelname
        self.year = year

    def display(self):
        print(self.modelname, self.year)
c1 = Car("Toyota", 2016)
c1.display()

#concept of class inheritance.

class Vehicle:
    def __init__(self, name,color,price):
        self.name = name
        self.color = color
        self.price = price

    def info(self):
        print(self.name, self.color, self.price)

class Car(Vehicle):

    def change_gear(self, no):
        print(self.name, 'change_gear', no)

#create object of car
car = Car('BMW','Black',35000)
car.info()
car.change_gear(5)















