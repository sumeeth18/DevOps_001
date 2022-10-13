#we can override method in python when same variable and values are equal
#defining parent class
#creating parent class
class Parent():
    #constructor 
    def __init__(self):
        self.value = 'Iside Parent'
    #Parents show method
    def show(self):
        print(self.value)
#creating class child
class Child(Parent):
    def __init__(self):
        self.value = 'Inside Child'
    def show(self):
        print(self.value)


obj1=Parent()
obj2=Child()
obj1.show()
obj2.show()

    

