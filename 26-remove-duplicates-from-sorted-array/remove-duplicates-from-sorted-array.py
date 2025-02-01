class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        k = 1  # First unique element is always at index 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # If the current element is unique
                nums[k] = nums[i]  # Place it at the correct position
                k += 1  # Increment the number of unique elements
        
        return k

