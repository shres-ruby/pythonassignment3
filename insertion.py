def insertion(ls):
    '''Performs insertion sort'''

    n = len(ls)
    for i in range(n):
        key = ls[i]
        j = i-1

        while j >= 0 and key < ls[j]:
            ls[j+1] = ls[j]
            j-=1

        ls[j+1] = key

    return ls


result = insertion([23,45,76,34,2,5,7,32])
print(result)