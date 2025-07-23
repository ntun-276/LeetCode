class Solution(object):
    def romanToInt(self, s):
        roman_mappings = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0

        for i in range(len(s)):
            if i < len(s) - 1 and roman_mappings[s[i]] < roman_mappings[s[i + 1]]:
                result -= roman_mappings[s[i]]
            else:
                result += roman_mappings[s[i]]

        return result

s = "MCMXCIV"
sol = Solution()
print(sol.romanToInt(s)) # Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.