def count_fun(no):
    cnt = 0
    while(int(no) > 0):
        cnt = cnt+1
        no = no/10

    return cnt


n = input("Enter number: ")
print(count_fun(int(n)))
