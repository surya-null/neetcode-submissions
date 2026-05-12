class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for n in nums:

            minHeap.append(n)
        heapq.heapify(minHeap)
        print(minHeap)
        res =0
        k = len(nums)-k
        print(k)
        while k>=0:

            res = heapq.heappop(minHeap)
            print(res)
            k-=1
        return res
