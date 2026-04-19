class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        max_len = 0
        start = 0

        i = 0
        while i < len(s):
            if s[i] in my_set:
                my_set.remove(s[start])
                start+=1
            else:
                my_set.add(s[i])
                max_len = max(max_len, len(my_set))
                i+=1
        
        return max_len