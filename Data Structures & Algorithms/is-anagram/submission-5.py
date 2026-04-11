class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {} # o(s)
        dict_t = {} # o(t)
        for char in s: # o(s)
            dict_s[char] = dict_s.get(char, 0)+1
        for char in t: # o(t)
            dict_t[char] = dict_t.get(char, 0)+1
        # o(s+t) space + o(s+t) time
        return dict_s==dict_t # o(s+t) if all key are different