# Needed:
# location of first digit
# location of 2nd digit
# current location in the list

class Solution:
    def twoSum(self, nums, target: int):
        numsdict = {}

        for i, n in enumerate(nums):
            compliment = target - n
            if compliment in numsdict:
                return [numsdict[compliment], i]
            else:
                numsdict[nums[i]] = i

class SolutionSorted:
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers) - 1

        while i < len(numbers):
            compliment = target - numbers[i]

            if numbers[j] == compliment:
                return [i + 1, j + 1]
            elif numbers[j] > compliment:
                j -= 1
            else:
                i += 1



solution = SolutionSorted()
print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([2, 3, 4], 6))
print(solution.twoSum([3, 3], 6))
print(solution.twoSum([1, 2, 3, 4], 6))


# revisited 4/19/22

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash = {}

        for i, n, in enumerate(nums):
            diff = target - n
            if diff in nums_hash:
                return [nums_hash[diff], i]
            nums_hash[n] = i

