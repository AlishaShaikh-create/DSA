def UnionSorted(nums1  , nums2):
    i = 0
    j = 0
    result = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j] :
            if not result or result[-1] != nums1[i]:
                result.append(nums1[i])
            i+=1
        else :
            if not result or result[-1] != nums2[j]:
                result.append(nums2[j])
            j+=1
    while i < len(nums1):
        if not result or result[-1]!= nums1[i]:
            result.append(nums1[i])
        i+=1

    while j < len(nums2):
        if not result or result[-1]!= nums2[j]:
            result.append(nums2[j])
        j+=1
    return result                                    

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 2, 7]
print(UnionSorted(nums1 , nums2))