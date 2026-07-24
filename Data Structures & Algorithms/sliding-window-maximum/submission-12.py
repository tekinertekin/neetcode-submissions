import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i in range(0,k):
            heapq.heappush(heap, -nums[i])
        ret = []
        for i in range(0,(len(nums) - k)):
            #print(-nums[i + k], -nums[i])
            ret.append(-heap[0])
            heapq.heappush(heap, -nums[i + k])
            heap.remove(-nums[i])
            heapq.heapify(heap)
        ret.append(-heap[0])
        return ret

        