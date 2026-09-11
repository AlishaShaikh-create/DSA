def leaders(nums):
    lead = []
    max_right = nums[len(nums)-1]
    lead.append(max_right)
    for i in range(len(nums)-2,-1,-1):
        if nums[i] > max_right:
            lead.append(nums[i])
            max_right = nums[i]
    lead = lead[::-1]
    return lead    

nums = [1, 2, 5, 3, 1, 2]
print(leaders(nums))

nums = [-3, 4, 5, 1, -4, -5]
print(leaders(nums))


nums = [-3, 4, 5, 1, -30, -10]
print(leaders(nums))

nums = [5,-4,-3,0,5]
print(leaders(nums))