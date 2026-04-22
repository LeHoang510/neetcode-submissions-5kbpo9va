class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, end = 0, 0
        my_dict = {}    # space O(1) because there is 26 chars 
        max_char = ("", 0) # space O(1)
        res = 0

        # time O(n)
        while end < len(s):
            my_dict[s[end]] = my_dict.get(s[end], 0) + 1
            if my_dict[s[end]] > max_char[1]:
                max_char = (s[end], my_dict[s[end]])
            while end - start + 1 - max_char[1] > k:
                my_dict[s[start]] -= 1
                start += 1
                
            res = max(res, end-start+1)
            end += 1
        # time O(n), space O(1)
        return res
