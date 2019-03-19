def primeCheck(no):
    # for i in range(0, len(arr)):
    # no = arr[i]
    flag = 0
    for i in range(2, no):
        if(no % i == 0):
            flag = 1
            break

    if(flag == 0):
        return True
    else:
        return False
