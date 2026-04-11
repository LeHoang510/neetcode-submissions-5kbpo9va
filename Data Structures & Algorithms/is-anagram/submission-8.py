class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # time O(nlogn+mlogm)
        # space O(1)
        return sorted(s)==sorted(t) 