def decimaltobinary(n):
    assert int(n)==n,'The Parameter must be an integer only!'
    if n==0:
        return 0
    else:
        return n%2+10*decimaltobinary(int(n/2))

print(decimaltobinary(10))