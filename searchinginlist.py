mylist=[1,2,3,4,5,6,7,8,9,10]

#in operator
if 10 in mylist:
    print(mylist.index(10))
else:
    print('The Value does not exist in the list.')

#Linear search
def searchinList(list,value):
    for i in list:
        if i == value:
            return list.index(value)
    return "The value does not exist in the list."

print(searchinList(mylist,100))