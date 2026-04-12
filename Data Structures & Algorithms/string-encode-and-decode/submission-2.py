class Solution:

    def encode(self, strs: List[str]) -> str:
        my_str = []
        # time O(n), space O(n)
        for s in strs:
            my_str.append(f"{len(s)}#"+s) 
        return "".join(my_str)

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        # time O(n), space O(n)
        while i<len(s):
            length = ""
            while s[i]!="#":
                length += s[i]
                i+=1
            length = int(length)
            i+=1
            word = "".join(s[i:i+length])
            i=i+length
            strs.append(word)

        return strs         