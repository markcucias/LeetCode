class Solution:
    def longestPalindrome(self, s: str) -> str:
        end = len(s)
        longest = s[0]
        for i in range(end):
            while s.rfind(s[i], i, end) != -1:
                temp = s[i: s.rfind(s[i], i, end) + 1]
                if temp == temp[::-1]:
                    if len(temp) > len(longest):
                        longest = temp
                    end = len(s)
                    break
                else:
                    end = s.rfind(s[i], i, end)
        return longest

