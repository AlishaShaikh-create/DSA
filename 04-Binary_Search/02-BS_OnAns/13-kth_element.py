def kth_element(a , b,k):
    if len(a) > len(b):
        a , b = b , a
    n = len(a)
    m = len(b)
    half = (n+m)//2
    low = 0
    high = n 
    while low <= high :
        partitionA = (low + high)//2
        partitionB = k - partitionA

        # Boundary Condition 
        if partitionA == 0:
            Aleft = float('-inf')
        else :
            Aleft = a[partitionA-1]

        if partitionA == n :
            Aright = float('inf')
        else :
            Aright = a[partitionA]

        if partitionB == 0:
            Bleft = float('-inf')
        else :
            Bleft = b[partitionB-1]
        
        if partitionB == m :
            Bright = float('inf')
        else :
            Bright = b[partitionB]    

        if Aleft <= Bright and Bleft <= Aright:
            return max(Aleft , Bleft)
        elif Aleft > Bright :
            high = partitionA -1
        else :
            low = partitionA + 1


a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10] 
k = 5 
print(kth_element(a,b,k))

a = [100, 112, 256, 349, 770] 
b = [72, 86, 113, 119, 265, 445, 892]
k = 7
print(kth_element(a,b,k))  