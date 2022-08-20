import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for value in stones:
            heappush(heap, (value * -1))
        
        while len(heap) > 1:
            y = heappop(heap) * -1
            x = heappop(heap) * -1
            
            if y == x:
                continue
            else:
                new_value = (y - x) * -1
                heappush(heap,new_value)
        if heap:
            return (heap[0] * -1)
        else:
            return 0
        