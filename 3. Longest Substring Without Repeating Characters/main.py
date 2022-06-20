class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp_str = ''
        temp_len = 0
        ans = 0
        for c in s:
            if c not in temp_str:
                temp_str += c
                temp_len += 1
            else:
                index = temp_str.index(c)
                temp_str = temp_str[index + 1:]
                temp_str += c
                temp_len = len(temp_str)
            if temp_len > ans:
                ans = temp_len
        return ans

solution = Solution()
print(solution.lengthOfLongestSubstring('dvdf'))
