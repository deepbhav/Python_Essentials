class Circle:

    PI = 3.142

    def __init__(self):
        self.area=0.0
        self.circumference=0.0
        self.radius=0.0
    
    def accept(self):
        rad=input("Enter the Radius : ")
        self.radius=float(rad)
    
    def findArea(self):
        self.area=Circle.PI*(self.radius*self.radius)

    def findCircumference(self):
        self.circumference=2*Circle.PI*self.radius

    def display(self):
        print("The Circle Contains one class Var- PI : ",Circle.PI)
        print("The Radius is : ",self.radius)
        print("The Area is : ",self.area)
        print("The Circumference is : ",self.circumference)

print("After Creating First Object: ")
obj=Circle()
obj.accept()
obj.findArea()
obj.findCircumference()
obj.display()

print("After Creating Second Object: ")
obj1=Circle()
obj1.accept()
obj1.findArea()
obj1.findCircumference()
obj1.display()


