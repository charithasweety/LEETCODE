#include <iostream>
using namespace std;

class Solution {
public:
    string countAndSay(int n) {
        if (n == 1) return "1";

        string result = "1"; // Base case

        for (int i = 2; i <= n; i++) {
            string temp = "";
            int count = 1;

            for (int j = 0; j < result.length(); j++) {
                if (j < result.length() - 1 && result[j] == result[j + 1]) {
                    count++;
                } else {
                    temp += to_string(count) + result[j];
                    count = 1; // Reset count
                }
            }
            result = temp; // Update for next iteration
        }

        return result;
    }
};
