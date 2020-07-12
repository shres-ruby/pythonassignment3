def linear(l,x):
    '''Performs a linear search'''

    for i in l:
        if x in l:
            return l.index(x)
    
        else:
            return -1

result = linear([3,6,4,8,1],4)
print(f'The index is {result}')