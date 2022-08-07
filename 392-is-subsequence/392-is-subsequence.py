class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        j=0 #j is the pointer of s
        for i in range(len(t)):
            if j == len(s):
                return True
            if t[i]==s[j]:
                j+=1
        return j == len(s)