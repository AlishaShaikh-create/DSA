# Brute force Approach :
class Solution:
    def singleNumber(self, nums):
        #your code goes here
        hashmap ={}
        result = 0
        for num in nums:
            if num in hashmap:
                hashmap[num]+= 1
            else :
                hashmap[num] = 1
        for key , value in hashmap.items():
            if value == 1:
                result = key
        return result   

