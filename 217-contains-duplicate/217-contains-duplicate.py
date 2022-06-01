class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        D = set()
        for x in nums:
            if x in D:
                return True
            D.add(x)
        return False