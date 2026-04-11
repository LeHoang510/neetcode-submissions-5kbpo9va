class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        list_s = list(s)
        list_t = list(t)
        for char in list_s:
            if char in list_t:
                list_t.remove(char)
            else:
                return False
        
        return True