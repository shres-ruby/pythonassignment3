def merge(l):
    '''Sort a list using merge sort'''
    n = len(l)
    if n == 1:
        return l
    
    elif n > 1:
        mid = n//2
        start = l[:mid]
        end = l[mid:]

        merge(start)
        merge(end)

        i=j=k=0

        while i<len(start) and j<len(end):
            if start[i] < end[j]:
                l[k] = start[i]
                i+=1
            
            else:
                l[k] = end[j]
                j+=1
            k+=1
        
        while i<len(start):
            l[k] = start[i]
            i+=1
            k+=1
        
        while j<len(end):
            l[k] = end[j]
            j+=1
            k+=1
    
    return l

result = merge([45,23,78,40,77,23,1,5])
print(result)