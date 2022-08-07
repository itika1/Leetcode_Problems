class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mydict=dict()
        val=""
        for i in range(len(s)):
            if s[i] not in mydict: #1st scenario
                if t[i] not in val:
                    mydict[s[i]]=t[i]
                    val+=t[i]
                else:
                    return False
            else:
                if mydict[s[i]]!=t[i]:
                    return False
        return True
                
                