def Longest_Subarray_Sum_k(nums , K):
    hashmap ={0:-1}
    current_sum = 0
    result = 0
    for i in range(len(nums)):
        current_sum += nums[i]
        previous_sum = current_sum -K
        if previous_sum in hashmap:
            length = i - hashmap[previous_sum]
            result = max(length , result)
            

        if current_sum not in hashmap:
            hashmap[current_sum] =i
        
    return result

nums = [10, 5, 2, 7, 1, 9]
k=15        
print(Longest_Subarray_Sum_k(nums , k))