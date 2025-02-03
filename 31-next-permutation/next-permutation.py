class Solution:
    def nextPermutation(self, nums):
        # Step 1: Find the first decreasing element from the right
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Step 2: If such an element is found, find the next larger element to swap
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 3: Reverse the elements to the right of i to get the next permutation
        nums[i + 1:] = reversed(nums[i + 1:])

# Example usage:
nums = [1, 2, 3]
Solution().nextPermutation(nums)
print(nums)  # Output: [1, 3, 2]
