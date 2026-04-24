class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l , r = 0, len(numbers)-1
        res =[]
        while l < r:

            twosum = numbers[l]+numbers[r]

            if twosum > target:

                r-=1
            elif twosum<target:
                l+=1
            else:
                res.append(l+1)
                res.append(r+1)
                l+=1
                r-=1
        return res