
try:
    fname=input("Enter filename ")
    fp=open(fname,"r")
    print("File Exists.")

except FileNotFoundError:
    print("File Not Exists.")

finally:
    fp.close()

# Output :
# PS I:\Assignments\Assignment8\Ass9> python .\Ass_9_1.py
# Enter filename MyFile1.txt
# File Not Exists.
# PS I:\Assignments\Assignment8\Ass9> python .\Ass_9_1.py
# Enter filename MyFile.txt
# File Exists