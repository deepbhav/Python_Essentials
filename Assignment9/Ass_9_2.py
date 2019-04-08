
try:
    fname=input("Enter filename ")
    fp=open(fname,"r")
    print("File Exists.")

    print("Contents of Files are: ")
    print(fp.read())

except FileNotFoundError:
    print("File Not Exists.")


finally:
    fp.close()
# Output
# PS I:\Assignments\Assignment8\Ass9> python .\Ass_9_2.py
# Enter filename MyFile.txt
# File Exists.
# Contents of Files are:
# Hello Deepak Bhavale is here.
# I am from Nashik!
# Hi
# Hello Bipin!
# How are you?