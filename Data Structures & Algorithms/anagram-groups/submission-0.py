class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute force
        res = {}

        for s in strs:
            key = "".join(sorted(s))
            if key not in res:
                res[key] = []

            res[key].append(s)
        
        m = [v for v in res.values()]

        return m
        
                    