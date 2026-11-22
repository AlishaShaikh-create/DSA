# Brute Force Approach :
# Generating the pascal triangle using for loop . time complexity is O(n2) and space complexity is O(n)

class Solution :
    def PascalTriangle(self , row):
        ans = 1
        ansRow = []
        ansRow.append(ans)
        for i in range(1,row):
            ans = ans * (row - i)
            ans = ans // i
            ansRow.append(ans)
        return ansRow
    def generate_PascalTriangle(self, n):
        result = []
        for row in range(1,n+1):
            result.append(self.PascalTriangle(row))
        return result

n = 4
c1 = Solution()
print(c1.generate_PascalTriangle(n))