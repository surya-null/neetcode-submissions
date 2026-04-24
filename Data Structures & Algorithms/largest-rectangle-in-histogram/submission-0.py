class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea=0

        stack=[] # index , height

        for i in range (len(heights)):

            start =i
            while stack and stack[-1][1] > heights[i]:

                currI, currH = stack.pop()

                maxarea = max((i-currI)*currH,maxarea)
                start= currI
            
            stack.append([start,heights[i]])
        
        while stack:
            currI, currH = stack.pop()

            maxarea = max((len(heights)-currI)*currH,maxarea)
        return maxarea
