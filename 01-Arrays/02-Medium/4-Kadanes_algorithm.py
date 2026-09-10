def kadanes_algorithm(nums):
    largest = float('-inf')
    for i in range(len(nums)):
        largest_sum = 0
        for j in range(i,len(nums)):
            largest_sum += nums[j]
            if largest_sum > largest:
                largest = largest_sum
    return largest

nums = [2, 3, 5, -2, 7, -4]
print(kadanes_algorithm(nums))  
nums = [-2, -3, -7, -2, -10, -4]
print(kadanes_algorithm(nums))    
nums = [-1, 2, 3, -1, 2, -6, 5]
print(kadanes_algorithm(nums))

# time - O(n2)
# space - O(1)

# kadanes Algorithm 
def kadanes_algorithm(nums):
    maximum = float('-inf')
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        maximum = max(sum , maximum)
        if sum < 0:
            sum = 0
        
    return maximum        

nums = [2, 3, 5, -2, 7, -4]
print(kadanes_algorithm(nums))  
nums = [-2, -3, -7, -2, -10, -4]
print(kadanes_algorithm(nums))    
nums = [-1, 2, 3, -1, 2, -6, 5]
print(kadanes_algorithm(nums))