# is Unique: Implement an algorithm to determine if a list has all unique characters,using python list.

import numpy as np

myArray=np.array([1,20,30,44,5,56,57,8,9,10,31,19,12,13,14,35,16,27,58,19,21])

def isunique(list):
    a=[]
    for i in list:
        if i in a:
            print(i)
            return False
        else:
            a.append(i)
    return True

print(isunique(myArray))