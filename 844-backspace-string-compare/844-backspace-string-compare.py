class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        S=[]
        T=[]
        for char in s:
            if char == '#':
                if len(S)>=1:
                    S.pop()
            else:
                S.append(char)
        for char in t:
            if char == '#':
                if len(T)>=1:
                    T.pop()
            else:
                T.append(char)
        return S==T
        