newtuple={'a','b','c','d','e'}

def searchInTuple(pTuple, element):
    for i in pTuple:
        if i == element:
            return pTuple.index(i)
    return 'The element does not exist'

print(searchInTuple(newtuple, 'a'))