from functools import *
arr=list()
def acceptFun(no):
    for i in range(0,no):
        num=input("Enter no : ")
        arr.append(num)
    return arr

def funCheck():
    for i in range(0,len(arr)):
        if(arr[i] >= 70):
            if (arr[i] <= 90):
                return arr[i]

no=input("Enter how many no :")
arr=acceptFun(int(no))
print("Before Filter Function :")
print(arr)

afterFilterList=list(filter(lambda no1: int(no1) >= 70 and int(no1) <= 90,arr))
print("After Filter Function :")
print(afterFilterList)

afterMapList=list(map(lambda no1 : int(no1) + 10,afterFilterList))
print("After Map Function :")
print(afterMapList)

afterReduce=reduce(lambda no1,no2 :int(no1)*int(no2),afterMapList)
print("The Multiplication is : ",afterReduce)

	#OutPut 
	#PS F:\MyPractice\Assignments\Python\Assignment_4> python .\Ass_4_3.py
	#Enter how many no :4
	#Enter no : 89
	#Enter no : 55
	#Enter no : 44
	#Enter no : 77
	#Before Filter Function :
	#['89', '55', '44', '77']
	#After Filter Function :
	#['89', '77']
	#After Map Function :
	#[99, 87]
	#The Multiplication is :  8613