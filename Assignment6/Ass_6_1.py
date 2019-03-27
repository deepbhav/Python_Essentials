def accept():
    no1=input("Enter first no: ")
    no2=input("Enter second no: ")
    return no1,no2

class Demo:
    value=10
    def __init__(self,no1,no2):
        self.x=no1
        self.y=no2

    def Fun(self):
        print("The value of First Instance var is : ",self.x)

    def Gun(self):
        print("The value of Second Instance var is :",self.y)

print("The class var value is ",Demo.value)
#Creating First Object
print("After Creating First Object : ")
no1,no2=accept()
obj=Demo(no1,no2)
obj.Fun()
obj.Gun()

print("After Creating Second Object : ")
#Creating Second Object
no1,no2=accept()
obj1=Demo(no1,no2)
obj1.Fun()
obj1.Gun()
