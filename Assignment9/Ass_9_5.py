import sys
import traceback

try :
    fp=open(sys.argv[1],"r")

    contents=fp.read()

    cnt=contents.count(input("Enter the tring to find Frequency :"))
    print("Occured :",cnt)

except FileNotFoundError as ex:
    print(ex)

finally:
    fp.close()
    
# Output
# PS I:\Assignments\Assignment8\Ass9> python .\Ass_9_5.py .\Demo1.txt
# [Errno 2] No such file or directory: '.\\Demo1.txt'
# PS I:\Assignments\Assignment8\Ass9> python .\Ass_9_5.py .\Demo.txt
# Enter the tring to find Frequency :Hello
# Occured : 2
# PS I:\Assignments\Assignment8\Ass9> cat .\Demo.txt
# Hello Deepak Bhavale is here.
# I am from Nashik!
# Hi
# Hello Bipin!
# How are you?
