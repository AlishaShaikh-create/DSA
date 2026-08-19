# Brute Force Approach :

def Finding_nth_root(n,m):
    for i in range(m):
        if i ** n == m :
            return i
        elif i ** n > m:
            break 
    return -1
N = 3
M = 27   
print(Finding_nth_root(N,M))     
N = 4
M = 69
print(Finding_nth_root(N, M))


print("--------------------------------")
# Optimal Solution
def Finding_nth_root(n,m):
    low = 0 
    high = m 
    while low <= high :
        mid = (low + high)//2
        if mid ** n == m :
            return mid 
        elif mid ** n < m :
            low = mid + 1
        else :
            high = mid -1 
    return -1 

N = 3
M = 27   
print(Finding_nth_root(N,M))     
N = 4
M = 69
print(Finding_nth_root(N, M))
    