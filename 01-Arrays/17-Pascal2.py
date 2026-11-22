# Brute Force Approach :
def PascalTriangle(r):
    result = []
    for i in range(r):
        final_array = []
        for j in range(i+1):
            if j == 0 or j == i:
                final_array.append(1)
            else :
                sum = result[i-1][j-1] + result[i-1][j]
                final_array.append(sum)
        result.append(final_array)
    return result[r-1]

r = 4
print(PascalTriangle(r))


# Optimal solution

def PascalTriangle2(nums,r):
    ans = [0]*r
    ans[0] = 1
    for i in range(1,r):
        ans[i] = (ans[i-1]*(r-i))//i
    return ans

r = 4
print(PascalTriangle(r))