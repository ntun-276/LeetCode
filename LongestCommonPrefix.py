class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return False

        min_length = min(len(s) for s in strs)
        common_prefix = ""

        for i in range(min_length):
            current_char = strs[0][i]

            if all(s[i] == current_char for s in strs):
                common_prefix += current_char
            else:
                break

        # for i in range(min_length):
        #     current_char = strs[0][i]
        #     flag = True
        #
        #     for s in strs:
        #         if current_char != s[i]:
        #             flag = False
        #
        #     if flag:
        #         common_prefix += current_char
        #     else:
        #         break

        return common_prefix

strs = ["flower","flow","flight"]
sol = Solution()
print(sol.longestCommonPrefix(strs)) # Output: fl