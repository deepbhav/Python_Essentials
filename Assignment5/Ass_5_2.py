strvar=''
cnt =1
def findNoOfWords(str):
    global cnt
    for i in range(0,len(str)):
        global strvar
        if(str[i]== ' '):
            cnt = cnt+1
    return cnt
accpetString=input("Enter the String : ")
print(findNoOfWords(accpetString))