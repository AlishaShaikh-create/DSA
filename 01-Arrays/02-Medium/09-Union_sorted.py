class Solution:
    def unionArray(self, nums1, nums2):
        i = 0
        j = 0
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j] :
                result.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i] < nums2[j] :
                result.append(nums1[i])
                i+=1
            elif nums2[j] > nums1[i] and result[-1] != nums2[j]:
                result.append(nums2[j])
                j+=1
        while i < len(nums1):
            if result[-1] != nums1[i]:
                result.append(nums1[i])
            i+=1
        while j < len(nums2):
            if result[-1] != nums2[j]:
                result.append(nums2[j])
            j+=1
        return result

s = Solution ()
nums1 = [3, 4, 6, 7, 9, 9]
nums2 = [1, 5, 7, 8, 8]
print(s.unionArray(nums1,nums2))


