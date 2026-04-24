class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map ={}

        for i in range(len(nums)):

            n = nums[i]
            if target-n in map:

                return [map[target-n],i]
            else:

                map[n]=i
        return [0,0]
        