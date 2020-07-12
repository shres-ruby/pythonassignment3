def bub(ls):
    '''Sort items in a list using bubble sort method'''
    
    for i in ls:
        for j in range(0,len(ls)-1):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
        
    return ls

result = bub([64, 34, 25, 12, 22, 11, 90])
print(result)
