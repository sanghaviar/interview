n = [1,2,3,4,5,6,7,8,9,10]
def evens(n):
    return n%2 == 0

e = list(filter(lambda n:n%2 ==0,n))
print(e)

