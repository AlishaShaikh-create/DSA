# Finding the Square Root of the number

# Brute Force approach :
def Finding_squareRoot(n):
    if n <= 1 :
        return n
    for i in range(2,n):
        if i * i == n:
            return i
        elif i * i > n :
            return i-1

n = 36
print(Finding_squareRoot(n))
n=28
print(Finding_squareRoot(n))   

# Optimal Solution
def Finding_squareRoots(n):
    low = 0
    high = n
    while low <= high:
        mid = (low + high)//2
        if mid * mid == n :
            return mid 
        elif mid * mid < n :
            ans = mid 
            low = mid + 1
        else :
            high = mid - 1
    return ans
print(Finding_squareRoots(28))            
print(Finding_squareRoots(36))            
    