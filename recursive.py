def findMaxNum(sampleArray,n):
    if n==1:
        return sampleArray[0]
    return max(sampleArray[n-1],findMaxNum(sampleArray,n-1))


def f(n):
    if n<=1:
        return 1
    return f(n-1)+f(n-1)

print(f(4))