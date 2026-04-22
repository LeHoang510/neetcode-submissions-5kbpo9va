class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, end = 0, 0
        my_dict = {}
        max_char = ("", 0)
        res = 0

        while end < len(s):
            my_dict[s[end]] = my_dict.get(s[end], 0) + 1
            if my_dict[s[end]] > max_char[1]:
                max_char = (s[end], my_dict[s[end]])
            while end - start + 1 - max_char[1] > k:
                my_dict[s[start]] -= 1
                start += 1
                
            res = max(res, end-start+1)
            end += 1

        return res
