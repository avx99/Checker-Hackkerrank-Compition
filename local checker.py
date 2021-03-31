import re
import numpy as np
import sys




def sumLigne(output):
    s = []
    for l in output:
        s.append(sum(l))
    return s


def sumColumne(output):
    s = []
    
    for j in range(len(output[0])):
        r = 0
        for i in range(len(output)):
            r = r + output[i][j]
        s.append(r)
    return s

def checkSum(output,arg1,arg2):
    a1 = sumLigne(output)
    a2 = sumColumne(output)
    return a1 == arg1 and a2 ==arg2


def neighbors(i , j) :
    """ find neighbors of a point"""
    ns = []
    # vector de direction
    dx = [+1, +1,  0, 1]
    dy = [0,  +1, 1,  -1]
    for d in range(4) :
        ns.append((i + dx[d], j + dy[d]))
    #remove neagative element
    ns = [i for i in ns if i[0] >= 0 and i[1] >= 0]
    return ns

def search(m, L, P, c) :
    
    c.append((L,P))
    Nset = neighbors(L, P)
    # remove out of range index
    Nset = [i for i in Nset if i[0] < len(m) and i[1] < len(m[0])]
    for  LP in Nset :
        if m[LP[0]][LP[1]] == 1:
            c = search(m, LP[0],LP[1], c)
    return c

def valid(t, comp) :
    """verify if a point is already visited"""
    for element in comp :
        if t in element :
            return False
    return True

def find_c(m):
    comp = []
    for L in range(len(m)) :
        for P in range(len(m[0])) :
            if m[L][P] == 1  and valid((L,P), comp):
                comp.append(search(m, L, P, []))
    return comp

def is_vert(e) :
    """verify if boat is vertical """
    f = e[0][0]
    for t in e :
        if f != t[0] :
            return False
    return True

def is_hori(e) :
    """verify if boat is horizantal """
    f = e[0][1]
    for t in e :
        if f != t[1] :
            return False
    return True

def check(m) :
    """check if the matrice is valid"""
    #find Connected-component
    lst = find_c(m)
    for e in lst :
        # verify len , 3 is the len of large boat
        if len(e) > 3 :
            return False
        if not is_vert(e) and  not is_hori(e):
            return False
    return True




try:
    result_data = open("test/25-25.txt", 'r').read()
except IOError:
    print("error in file of your output")

lst = [l.rstrip() for l in result_data.split('\n')]
lst = [i.split(' ') for i in lst]
while [''] in lst:
    lst.remove([''])
output = [list(map(int,l)) for l in lst]
np_arr = np.array(output)


try:
    arg = open("test/test 25-25.txt", 'r').read()
except IOError:
    print("error in arrguments file")
    
arg = [l.rstrip() for l in arg.split('\n')]
arg = [i.split(' ') for i in arg]
while [''] in arg:
    arg.remove([''])
arg = [list(map(int,l)) for l in arg]


if check(output) and checkSum(output,arg[0],arg[1]) :
    sys.stderr.write('\x1b[1;32m' + "------OK------".strip() + '\x1b[0m' )
else :
    sys.stderr.write('\x1b[1;31m' + "----KO------".strip() + '\x1b[0m' )





import numpy
import matplotlib.pyplot as plt
np_output = np.array(output)
im = plt.imshow(np_output)


arg2 = np.sum(np_output,axis=0)
arg1 = np.sum(np_output,axis=1)


# f = open("test/test 200-150.txt", "w")
# for i in arg1:
#     f.write(str(i))
#     f.write(' ')
# f.write('\n')
# for i in arg2:
#     f.write(str(i))
#     f.write(' ')
# f.close()





a = np.array([2,5,6])
b = np.array([2,2,6])

xxx= sumLigne(output)
yyy = sumColumne(output)

