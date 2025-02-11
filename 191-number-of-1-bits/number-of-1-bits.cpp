class Solution {
public:
    int hammingWeight(int n) {
        int count = 0;
        while (n) {
            count += (n & 1);  // Check if last bit is 1
            n >>= 1;           // Shift bits to the right
        }
        return count;
    }
};
