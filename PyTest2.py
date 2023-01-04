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
















