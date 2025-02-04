class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Check if we found the target
            if nums[mid] == target:
                return mid
            
            # Determine which part is sorted
            if nums[left] <= nums[mid]:
                # Left part is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target is in the left part
                else:
                    left = mid + 1  # Target is in the right part
            else:
                # Right part is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # Target is in the right part
                else:
                    right = mid - 1  # Target is in the left part
        
        return -1  # Target not found

# Example usage:
sol = Solution()
nums1 = [4, 5, 6, 7, 0, 1, 2]
target1 = 0
print(sol.search(nums1, target1))  # Output: 4

nums2 = [4, 5, 6, 7, 0, 1, 2]
target2 = 3
print(sol.search(nums2, target2))  # Output: -1

nums3 = [1]
target3 = 0
print(sol.search(nums3, target3))  # Output: -1
