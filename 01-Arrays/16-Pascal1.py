# Pascal Triangle - 1

# Brute force approach
result = []
n = 4
for i in range(0,n):
    new_arr = []
    for j in range(i+1):
        if j == 0 or j == i:
            new_arr.append(1)
        else :
            final = result[i-1][j-1] + result[i-1][j]
            new_arr.append(final)
    result.append(new_arr)
print(result)

def pascalTriangle(r,c):
    n = r
    result =  []
    for i in range(n):
        new_array =  []
        for j in range(i+1):
            if j == 0 or j == i:
                new_array.append(1)
            else:
                final = result[i-1][j-1] + result[i-1][j]
                new_array.append(final)
        result.append(new_array)
    return result[r-1][c-1]

r = 4
c = 2
print(pascalTriangle(r,c))


# Optimal Solution :
# Approach :
# -> Find the ncr will give the element at that position .
class Solution :
    def pascalTriangle(self , r , c):
        return self.ncr(r-1 , c-r)
    
    def ncr(self ,n,r):
        if r > n - r:
            r = n - r
        
        res = 1
        for i in range(r):
            res = res * ( n - i)
            res = res // (i+1)
        return res
            
r = 4
c = 2
print(pascalTriangle(r,c))    
