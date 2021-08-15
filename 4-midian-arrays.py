# Given two sorted arrays: num1 & num2
# return the median of the two sorted arrays
# Constraints: O() == O(log (m+n))
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5
#
# understandings: if even, median is (middle 2 numbers / 2)
# if odd, middle number

# This is the naive O(m + n), _NOT_ O(log (m+n))
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merged = sorted(nums1 + nums2)

        merged = [float(i) for i in merged]

        #print(merged)

        middle = len(merged) // 2
        #print(merged[middle - 1])
        #print(merged[middle])
        if (len(merged) % 2 == 0):
            #print((merged[middle - 1] + merged[middle]) / 2)
            return ((merged[middle - 1] + merged[middle]) / 2)
        else:
            #print(merged[middle])
            return (merged[middle])


solution = Solution()
#solution.findMedianSortedArrays([1, 3], [2]) # -> [1, 2, 3], median == 2.0
#solution.findMedianSortedArrays([1, 2], [3, 4]) # -> [1, 2, 3, 4], median == 2.5
#solution.findMedianSortedArrays([0, 0], [0, 0]) # -> median == 0.0
#solution.findMedianSortedArrays([], [1]) # -> median == 1.00
#solution.findMedianSortedArrays([2], []) # -> median == 2.00
solution.findMedianSortedArrays([1, 3], [2, 7]) # -> median == 2.50

