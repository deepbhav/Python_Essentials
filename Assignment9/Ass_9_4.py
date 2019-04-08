import sys
import traceback


try :

    fp=open(sys.argv[1],"r")
    fd=open(sys.argv[2],"r")

    firstFileContents=fp.read()
    secondFileContents=fd.read()

    if(firstFileContents==secondFileContents):
        print("Both the files have Identical Contents")
    else:
        print("Both the files dont have Identical Contents")


except Exception as ex:
    print(ex)

finally:
    fp.close()
    fd.close()
    
# Output :

# PS I:\Assignments\Assignment8\Ass9> python .\Ass_9_4.py .\Demo.txt .\MyFile.txt
# Both the files dont have Identical Contents
# PS I:\Assignments\Assignment8\Ass9> python .\Ass_9_4.py .\Demo.txt .\MyFile.txt
# Both the files have Identical Contents
# PS I:\Assignments\Assignment8\Ass9> python .\Ass_9_4.py .\Demo.txt .\MyFile1.txt
# [Errno 2] No such file or directory: '.\\MyFile1.txt'
# PS I:\Assignments\Assignment8\Ass9> python .\Ass_9_4.py .\Demo1.txt .\MyFile.txt
# [Errno 2] No such file or directory: '.\\Demo1.txt'
# PS I:\Assignments\Assignment8\Ass9> python .\Ass_9_4.py .\Demo1.txt .\MyFile1.txt
# [Errno 2] No such file or directory: '.\\Demo1.txt'