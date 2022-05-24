class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        mini_diff = abs(arr[0] - arr[1])
        result = []
        
        for i in range(len(arr)-1):
            diff = abs(arr[i] - arr[i+1])
            
            if result and diff < mini_diff:
                mini_diff = diff
                result = []
                result.append([arr[i], arr[i+1]])
                
            elif diff <= mini_diff:
                mini_diff = diff
                result.append([arr[i], arr[i+1]])
                
        return result