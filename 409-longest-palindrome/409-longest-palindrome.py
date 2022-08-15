class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic= collections.Counter(s)
        res=0
        flag=False
        for key,val in dic.items():
            if val%2==0:
                res+=val
            else:
                if flag:
                    res+=val-1
                else:
                    flag=True
                    res+=val
        return res
        