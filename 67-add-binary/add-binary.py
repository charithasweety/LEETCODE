class Solution:
    def addBinary(self, a, b):
        result = ""
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            sum_val = carry
            if i >= 0:
                sum_val += int(a[i])
                i -= 1
            if j >= 0:
                sum_val += int(b[j])
                j -= 1

            result = str(sum_val % 2) + result
            carry = sum_val // 2

        return result

# Example usage
# Uncomment these lines if running locally
# a = input().strip()
# b = input().strip()
# print(Solution().addBinary(a, b))
