class Solution:
    def fourSum(self, nums, target):
        nums.sort()  # Sort the array to make it easier to handle duplicates and use two-pointer technique
        n = len(nums)
        result = []
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for the first number
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicates for the second number
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:  # Skip duplicates for the third number
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:  # Skip duplicates for the fourth number
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return result
