#plus operator
a=[1,2,3]
b=[4,5,6]

c=a+b
print(c)

# star(*) operator
d=[1,2]
d=d*2
print(d)

#len function
e=[1,2,3,6,5,4]
print(len(e))

#max function
print(max(e))

#min function
print(min(a))

#sum() function
print(sum(e))

#average of list number

mylist=list()
while(True):
    inp=input("Enter a number: ")
    if inp == 'done':break
    Value=float(inp)
    mylist.append(Value)
Average=sum(mylist)/len(mylist)

print('Average',Average)