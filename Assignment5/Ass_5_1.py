
# Solution 1

# s = ''
# def reverseString(str):
#     global s
#     for i in str:
#         s = i + s
#     return s

# Solution 2

strvar=''
def reverseString(str):
    for i in range(len(str)-1,-1,-1):
        global strvar
        strvar= strvar + str[i]
    return strvar

acceptStr=input("Enter the String : ")
print(reverseString(acceptStr))


#Output
# PS E:\Assignments\Python\Assignment-5> python .\Ass_5_1.py
# Enter the String : Deepak Bhavale is here, from Nashik
# kihsaN morf ,ereh si elavahB kapeeD