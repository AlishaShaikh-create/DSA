def Kth_missing_positive_number(nums,k):
    i = 1 
    missing = 0
    
    while i :
        if i not in nums:
            missing+=1
        if missing == k:
            return i  
        i+=1  


arr = [3, 5, 7, 10] 
k = 6
print(Kth_missing_positive_number(arr,k))   
arr = [1, 2, 3]
k = 5
print(Kth_missing_positive_number(arr,k))  

# time - O(n*k)
print("-----------------------------------------")
def Kth_missing_positive_number(nums,k):
    prev = 0
    for num in nums:
        missing = num - prev -1 
        # if the missing number lies inside the range
        if k <= missing :
            return prev + k
        k -= missing 
        prev =  num
    # if the missing number lies beyond the maximum element in the array     
    return prev + k     
arr = [3, 5, 7, 10] 
k = 6
print(Kth_missing_positive_number(arr,k))   
arr = [1, 2, 3]
k = 5
print(Kth_missing_positive_number(arr,k))  

print("-----------------------------------------")
def Kth_missing_positive_number(nums,k):
    low = 0
    high = len(nums)
    for
