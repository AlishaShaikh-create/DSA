def Buy_Sell_Stock(nums):
    max_profit = 0
    for i in range(len(nums)):
        profit  = 0
        for j in range(i+1,len(nums)):
            if nums[j] > nums[i]:
                profit = nums[j]-nums[i]
                max_profit = max(max_profit , profit)
    return max_profit
arr = [10, 7, 5, 8, 11, 9]
print(Buy_Sell_Stock(arr))            
arr = [5, 4, 3, 2, 1]
print(Buy_Sell_Stock(arr)) 

def Buy_Sell_Stock(nums):
    max_profit = 0
    min_price = nums[0]
    for i in range(1,len(nums)):
        if nums[i] > min_price:
            profit = nums[i] - min_price
            max_profit = max(max_profit,profit)
        min_price = min(nums[i], min_price)
    return max_profit
arr = [10, 7, 5, 8, 11, 9]
print(Buy_Sell_Stock(arr))            
arr = [5, 4, 3, 2, 1]
print(Buy_Sell_Stock(arr))    
        