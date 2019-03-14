def count_fun(no):
    cnt = 0
    rem = 0
    sum = 0
    while(int(no) > 0):
        rem = no % 10
        sum = sum+int(rem)
        no = int(no)/10
    return int(sum)


n = input("Enter number: ")
print(count_fun(int(n)))
