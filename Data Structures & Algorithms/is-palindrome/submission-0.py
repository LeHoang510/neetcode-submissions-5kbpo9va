class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()  # O(n)
        l = len(s)
        i = 0
        # O(n/2)
        while i < l//2:
            if s[i]!=s[l-1-i]:
                return False
            i+=1
        return True