def roseGarden(n , nums , k , m):
    if m * k > n :
        return -1 
    for day in range(min(nums),max(nums)+1):
        consecutive = 0
        bouquet  =0 
        for i in range(len(nums)):
            if nums[i] <= day :
                consecutive +=1
                if consecutive == k :
                    bouquet+=1
                    consecutive =0 

            else :
                consecutive = 0  
        if bouquet >= m :
            return day
    return -1               

print("---------------------------------------")
# Optimal Solution
def roseGarden(n , nums , k , m):
    if m * k > n :
        return -1 
    low = min(nums)
    high = max(nums)
    ans =  -1 
    while low <= high :
        mid = (low + high)//2
        consecutive = 0
        bouquet = 0
        for i in range(len(nums)):
            if nums[i] <= mid :
                consecutive += 1
                if consecutive ==  k :
                    bouquet += 1
                    consecutive = 0
            else : 
                consecutive = 0
        if bouquet >= m :
            ans  = mid 
            high = mid - 1 
        else :
            low = mid + 1
    return ans 

n = 8
nums = [7, 7, 7, 7, 13, 11, 12, 7]
m = 2
k = 3                            
print(roseGarden(n , nums , k ,m))

n = 5
nums = [1, 10, 3, 10, 2]
m = 3
k = 2    
print(roseGarden(n , nums , k ,m))

nums = [62,75,98,63,47,65,51,87,22,27,73,92,76,44,13,90,100,85]
m = 2
k = 7
print(roseGarden(len(nums) , nums, k , m))