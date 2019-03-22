from itertools import permutations 

# Solution 1 - For String Reverse

# s = ''
# def reverseString(str):
#     global s
#     for i in str:
#         s = i + s
#     return s

# Solution 2 - For String Reverse

strvar=''
def reverseString(str):
    for i in range(len(str)-1,-1,-1):
        global strvar
        strvar= strvar + str[i]
    return strvar


strvar=''
cnt =1
def findNoOfWords(str):
    global cnt
    for i in range(0,len(str)):
        global strvar
        if(str[i]== ' '):
            cnt = cnt+1
    return cnt

def findCombinantions(str):
    cnt = 0
    perm = permutations(str) 
    for i in list(perm):
        cnt = cnt + 1
        print(i)
    print("Total Combinations are : {}".format(cnt))

def deleteByPosition(str,key):
        newl=list(str)
        del(newl[key-1])
        s = "".join(newl)
        return s

def addASCIIForString(str):
    newStr=list(str)
    sum =0
    for i in range(len(newStr)):
        print("Char {} = ASCII {}.".format(newStr[i],ord(newStr[i])))
        sum = sum + ord(newStr[i])
    return sum,len(newStr)