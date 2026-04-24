from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         res = defaultdict(list)
         for s in strs:
            arr =[0]*26
            for ch in s:
                arr[ord(ch)-ord('a')] +=1

            key = tuple(arr)
            res[key].append(s)
         return list(res.values())