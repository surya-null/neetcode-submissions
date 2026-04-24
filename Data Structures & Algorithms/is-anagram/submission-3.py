class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        mapST ,mapTS ={},{}

        if len(s) != len(t):
            return False
        
        for ch in s:
            mapST[ch]=1+mapST.get(ch,0)
        
        for ch in t:

            mapTS[ch]=1+mapTS.get(ch,0)
            
        
        if mapTS == mapST:
            return True
        return False

