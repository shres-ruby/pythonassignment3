def inter(ls,x):
    '''Performs interpolation search'''

    low = 0
    high = len(ls)-1

    while low <= high:
        p = low + (high-low) * (x-ls[low]) // (ls[high]-ls[low])

        if x == ls[p]:
            return p

        elif x > ls[p]:
            low = p+1
        
        else:
            high = p-1

result = inter([44,60,75,100,120,230,250],100)
print(result)