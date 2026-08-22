def Search_2D_Array(mat , target):
    if not mat or not mat[0]:
        return False
    r = len(mat)
    c = len(mat[0])
    low  = 0
    high = (r *c )-1
    while low <= high :
        mid = (low + high)//2
        row = mid // c
        column =  mid % c
        if mat[row][column] == target :
            return True
        elif mat[row][column] < target :
            low = mid + 1
        else :
            high = mid - 1
    return False            

mat  = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]
target = 8
print(Search_2D_Array(mat , target))

mat = [ [1, 2, 4], [6, 7, 8], [9, 10, 34] ]
target = 78
print(Search_2D_Array(mat , target))


    