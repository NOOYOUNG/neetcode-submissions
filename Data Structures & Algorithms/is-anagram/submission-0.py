class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashS = {}
        hashT = {}

        for sstr in s:
            hashS[sstr] = hashS.get(sstr, 0) + 1

        for tstr in t:
            hashT[tstr] = hashT.get(tstr, 0) + 1

        return hashS == hashT