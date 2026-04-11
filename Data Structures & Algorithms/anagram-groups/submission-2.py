class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute force
        # space O(nk)
        res = {}

        # O(n)
        for s in strs:
            key = "".join(sorted(s)) # O(klogk)
            if key not in res: # O(1)
                res[key] = []

            res[key].append(s) # O(1)
        # => O(n klogk)
        m = [v for v in res.values()]   # O(n)

        return m
        
                    