class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == [""]:
            return ""
        
        w = strs[0]
        
        for l in range(len(w)):
            b = w[:l+1]
            if sum([s.startswith(b) for s in strs]) != len(strs):
                return b[:-1]
        return w   