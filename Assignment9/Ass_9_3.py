import sys

try:
    fp=open("Demo.txt","w")
    filename=sys.argv[1]
    fd=open(filename,"r")
    contents=fd.read()
    fp.write(contents)

except FileNotFoundError:
    print("File Not Exists.")

finally:
    fp.close()
    fd.close()
    
# Output

# PS I:\Assignments\Assignment8\Ass9> python .\Ass_9_3.py .\MyFile1.txt
# File Not Exists.
# PS I:\Assignments\Assignment8\Ass9> python .\Ass_9_3.py .\MyFile.txt
# PS I:\Assignments\Assignment8\Ass9> cat .\Demo.txt
# Hello Deepak Bhavale is here.
# I am from Nashik!
# Hi
# Hello Bipin!
# How are you?