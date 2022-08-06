class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum=0
        lst=[]
        for i in nums:
            sum=sum+i
            lst.append(sum)
        return lst