class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        
        res =[]
        def dfs(i,curr, total):

            if total == target:
                res.append(curr.copy())
                return
            
            if i>=len(nums) or total > target:
                return
            

            # choosing the i index

            curr.append(nums[i])

            dfs(i,curr,total+nums[i])

            # removing the i index from current list and choosing the next index
            curr.pop()

            dfs(i+1,curr,total)
        
        dfs(0,[],0)

        return res