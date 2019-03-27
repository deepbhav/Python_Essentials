class Arithmatic:
    
    def __init__(self):
        self.ans=0

    def Accept(self):
        no1=input("Enter first no: ")
        no2=input("Enter second no: ")
        self.x=int(no1)
        self.y=int(no2)

    def Add(self):
        self.ans=self.x+self.y
        print("The Addtion is : ",self.ans)

    def Sub(self):
        self.ans=self.x-self.y
        print("The Subtraction is : ",self.ans)

    def Mult(self):
        self.ans=self.x*self.y
        print("The Multiplication is : ",self.ans)

    def Div(self):
        self.ans=self.x/self.y
        print("The Division is : ",float(self.ans))


print("#First Object Creation : ")
#First Object Creation :
obj=Arithmatic()
obj.Accept()
obj.Add()
obj.Sub()
obj.Mult()
obj.Div()

print("#Second Object Creation : ")
#Second Object Creation :
obj1=Arithmatic()
obj1.Accept()
obj1.Add()
obj1.Sub()
obj1.Mult()
obj1.Div()