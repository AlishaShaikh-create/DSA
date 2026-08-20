# Median of the 2 sorted array 
def median_sorted(arr1 , arr2):
    i  = 0
    j  = 0
    temp = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            temp.append(arr1[i])
            i+=1
        else :
            temp.append(arr2[j])
            j+=1
    while i < len(arr1):
        temp.append(arr1[i])
        i+=1
    while j < len(arr2):
        temp.append(arr2[j])
        j+=1
    
    n = len(temp)
    if n % 2 == 0 :
        mid = n // 2
        median = (temp[mid-1] + temp[mid])/2
    else :
        median = temp[n//2]

    return median

arr1 = [2, 4, 6]
arr2 = [1, 3, 5]
print(median_sorted(arr1, arr2))
arr1 = [2, 4, 6] 
arr2 = [1, 3]
print(median_sorted(arr1,arr2))

