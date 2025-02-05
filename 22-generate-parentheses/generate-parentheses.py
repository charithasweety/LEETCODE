class Solution:
    def generateParenthesis(self, n):
        def backtrack(s, left, right):
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)

        result = []
        backtrack('', 0, 0)
        return result

# Test the function with the examples
solution = Solution()
print(solution.generateParenthesis(3))  # Example 1
print(solution.generateParenthesis(1))  # Example 2
