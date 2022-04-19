class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        # handles single value in array (either at start or after iterations)
        while l <= r:
            candidate_index = (l + r) // 2

            if nums[candidate_index] == target:
                return candidate_index
            elif target > nums[candidate_index]:
                l = candidate_index + 1
            else:
                r = candidate_index - 1

        return -1

