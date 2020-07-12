def quicksort(ls):
    '''Sort a list using quicksort method'''

    n = len(ls)

    if n == 1:
        return ls

    else:
        pivot = ls[n-1]
        left = []
        right = []
        
        for i in range(0,n-1):
            if ls[i] < pivot:
                left.append(ls[i])

            else:
                right.append(ls[i])

        return left+[pivot]+right


result = quicksort([64,67,23,70,98,32])
print(result)