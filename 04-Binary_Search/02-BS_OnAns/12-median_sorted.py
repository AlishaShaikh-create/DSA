# Median of the 2 sorted array 
# Brute Force approach 
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

print("--------------------------------------")
# Optimal Approach
def median_sorted(A , B):
    if len(A) > len(B):
        A,B = B , A
    n =  len(A)
    m =  len(B)
    half = ( n + m)//2
    low = 0
    high = n 
    while low <= high :
        partitionA = (low + high)//2
        partitionB = half - partitionA 

        # Boundary Condition check :
        if partitionA == 0:
            Aleft = float('-inf')
        else :
            Aleft = A[partitionA-1]

        if partitionA == n :
            Aright = float('inf')
        else :
            Aright = A[partitionA]

        if partitionB == 0:
            Bleft = float('-inf')
        else :
            Bleft = B[partitionB-1]
        
        if partitionB == n :
            Bright = float('inf')
        else :
            Bright = B[partitionB]

        if Aleft <= Bright and Bleft <= Aright:
            # if all the elements are odd
            if  (n+m)%2 == 1 :
                return min(Aright , Bright)
            else :
                left_max = max(Aleft , Bleft)
                right_min = min(Bright , Aright)
                return (left_max + right_min)/2
        elif Aleft > Bright:
            high = partitionA-1
        else :
            low = partitionA+1
A = [1, 2]
B = [3, 4, 5, 6]
print(median_sorted(A , B))  
      


