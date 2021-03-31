import re
import numpy as np
import sys


try:
    result_data = open("output.txt", 'r').read()
except IOError:
    print("error in file of your output")

lst = result_data.split('\n')
lst = [i.split(' ') for i in lst]
output = [list(map(int,l)) for l in lst]
np_arr = np.array(output)


try:
    arg = open("arr.txt", 'r').read()
except IOError:
    print("error in arrguments file")
    
arg = arg.split('\n')
arg = [i.split(' ') for i in arg]
arg = [list(map(int,l)) for l in arg]




def checkH(X,i,j):
    if i < n-1 :
        if X[i+1][j] == 1:
            return False
    
    if j < p - 1:  
        if X[i][j+1] == 0:
            return True

    if i == n-1 and j == n-1:
        return True

    return checkH(X,i,j+1)
    
def checkV(X,i,j):
    if i < n-1 :
        if X[i+1][j] == 0:
            return True
    
    if j < p - 1:  
        if X[i][j+1] == 1:
            return False
    
    if i == n-1 and j == n-1:
        return True

    return checkV(X,i+1,j)
    
        

def checker(X):
    global n 
    global p 
    
    n = len(X)
    p = len(X[0])
    
    for i in range(n):
        for j in range(p):
            if X[i][j] == 1:
                print(i," , ",j)
                if j < p - 1:
                    if X[i][j + 1] == 1:
                        hc = checkH(X,i,j+1)
                        print("hor: ",i," , ",j,":", hc)
                        if hc == False :
                            return False
                if i < n-1:
                    if X[i+1][j] == 1:
                        hv = checkV(X,i,j+1)
                        print("vert: ",i," , ",j,":", hv)
                        if hv == False :
                            return False
    
    return True
                    
X = [[1,0,0,0,0,0],[1,0,0,1,0,1],[0,0,0,1,0,0],[0,0,0,0,0,0],[1,0,1,1,1,0],[1,0,0,0,0,0]]

d=checker(output) # valid
print("X :",d)

# print("*****************************************")

# Y = [[1,0,0,0,0,0],[1,0,0,1,0,1],[0,1,0,1,0,0],[0,0,0,0,0,0],[1,0,1,1,1,0],[1,0,1,1,0,0]]

# d=checker(Y) # invalid
# print("Y :",d)               