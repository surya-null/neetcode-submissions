class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        beg =1 
        end = max(piles)
        res = 999999999999
        qty = max(piles)
        while beg <=end:

            mid = (beg+end)//2
            hours =0
            for p in piles:
                hours+=math.ceil(p/mid)
            
            if hours<=h:
                res = min(mid,res)
                end = mid-1
            else:
                beg = mid+1
        return res
                    