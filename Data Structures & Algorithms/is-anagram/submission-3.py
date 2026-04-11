class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        list_s = list(s) # o(n) time and space
        list_t = list(t) 
        for char in list_s: # o(n)
            if char in list_t:
                list_t.remove(char) # o(n)
            else:
                return False
        # o(n^2) time o(n) space
        return True