def cal_length(str):
    cnt = 0 
    for i in str:
        cnt = cnt + 1
    return cnt

s=input("Enter String :")
print(cal_length(s))