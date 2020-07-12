def binary(l,x):
    '''Performs binary search for an element in a list'''

    n = len(l)
    mid = n//2

    if x == l[mid]:
        return mid

    elif x < l[mid]:
        return binary(l[:mid+1],x)
    
    else:
        return mid + binary(l[mid:],x)
        

result = binary([3,5,7,8,9,10,88,78,90,56],90)
print(result)