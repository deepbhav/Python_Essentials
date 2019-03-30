class Numbers:
    def __init__(self):
        no=input("Enter the no: ")
        self.value=int(no)

    def checkPrime(self):
        pno=self.value
        for i in range(2,pno):
            if((pno%i) == 0):
                return False
            else:
                return True

    def factors(self):
        l=list()
        for i in range(1,self.value):
            if((self.value%i)==0):
                l.append(i)
        return l

    def factorsSum(self,l):
        sum = 0
        for i in range(0,len(l)):
           sum = sum + ll[i]
        return sum

obj=Numbers()
print(obj.checkPrime())
ll=obj.factors()
print(ll)
print(obj.factorsSum(ll))


obj1=Numbers()
print(obj1.checkPrime())
ll=obj1.factors()
print(ll)
print(obj1.factorsSum(ll))


# Output:
# PS I:\Assignments\Assignment-9> python .\Ass_7_3.py
# Enter the no: 22
# False
# [1, 2, 11]
# 14
# Enter the no: 6
# False
# [1, 2, 3]
# 6