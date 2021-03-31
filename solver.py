import os


def getArguments(path='test'):
    lst = []
    dl = os.listdir(path)
    for i in dl:
        if i.startswith('test '):
            with open(path+'/'+i,'r') as f:
                lines = f.readlines()
                lines = [l.rstrip().split(' ') for l in lines]
                lst.append(lines)
    return lst



def getOutputs(path='test'):
    lst = []
    dl = os.listdir(path)
    for i in dl:
        if not i.startswith('test'):
            print(i)
            with open(path+'/'+i,'r') as f:
                lines = f.read()
                print(lines)
                print('------------------------------------------')
            lst.append(lines)
    return lst

lst = getArguments()
lll = getOutputs()