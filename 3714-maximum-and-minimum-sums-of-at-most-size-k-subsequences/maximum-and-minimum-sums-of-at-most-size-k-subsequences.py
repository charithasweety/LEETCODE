MOD = 10**9 + 7

class Solution:
    def binomial(self, n, k, fact, inv_fact):
        if k > n or k < 0:
            return 0
        return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

    def minMaxSums(self, nums, k):
        n = len(nums)
        nums.sort()

        # Precompute factorials and their modular inverses
        fact = [1] * (n + 1)
        inv_fact = [1] * (n + 1)
        
        # Compute all factorials % MOD
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        
        # Compute inverses using Fermat's Little Theorem
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, 0, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
        
        max_sum = 0
        min_sum = 0
        
        # Iterate through the sorted nums to calculate contributions
        for i in range(n):
            # Contributions of nums[i] as maximum element
            max_contrib = nums[i] * sum(self.binomial(i, j, fact, inv_fact) for j in range(0, k)) % MOD

            # Contributions of nums[i] as minimum element
            min_contrib = nums[i] * sum(self.binomial(n - i - 1, j, fact, inv_fact) for j in range(0, k)) % MOD

            max_sum = (max_sum + max_contrib) % MOD
            min_sum = (min_sum + min_contrib) % MOD

        return (max_sum + min_sum) % MOD

# Example usage:
nums = [1, 2, 3]
k = 2
solution = Solution()
result = solution.minMaxSums(nums, k)
print(result)  # Expected output: 24
