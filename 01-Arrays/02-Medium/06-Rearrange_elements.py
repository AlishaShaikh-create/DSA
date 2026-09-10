def Rearrange_Elements(nums):
    pos = 0
    neg = 1
    ans = [0]*len(nums)
    for i in range(len(nums)):
        if nums[i] > 0:
            ans[pos] = nums[i]
            pos+=2
        else :
            ans[neg] = nums[i]
            neg+=2
    return ans
nums = [2, 4, 5, -1, -3, -4]
print(Rearrange_Elements(nums))   
