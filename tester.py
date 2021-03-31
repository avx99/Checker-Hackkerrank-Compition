import re
import numpy as np
import sys

try:
    result_data = open("test/25-25.txt", 'r').readlines()
except IOError:
    print("error in file of your output")
    
    
f = open("test/tester/tester 25-25.txt", "w")
for i in result_data:
    f.write('    fptr.write('+'\''+i.rstrip()+'\''+' + \'\\n\''+')'+'\n')
    

# f.writelines(result_data)
f.close()

