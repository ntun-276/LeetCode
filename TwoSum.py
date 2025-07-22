class Solution(object):
    # O(n^2)
    def twoSum(self, nums, target):
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    # O(n)
    def twoSum2(self, nums, target):
        num_dict = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []

# Example
nums = [2, 7, 11, 15]
target = 9

sol = Solution()
print(sol.twoSum(nums, target)) # Output: [0, 1]