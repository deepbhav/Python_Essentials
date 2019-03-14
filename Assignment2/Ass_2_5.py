def check_Prime(no):
    flag = 1
    for i in range(2, no+1):
        if(no % i) == 0:
            flag = 0
            break
        return flag


n = input("Input no to check: ")
if(check_Prime(int(n)) == 1):
    print("It is a prime number")
else:
    print("It is Not prime number")
