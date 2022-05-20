class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #digits=digits[::-1]
        #carry,i=1,0
        #while carry:
         #   if i<len(digits):
          #      if digits[i]==9:
           #         digits[i]=0
            #    else:
             #       digits[i]+=1
            #else:
             #   digits.append(1)
              #  one=0
            #i+=1
        #return digits[::-1]
        s = [str(i) for i in digits]
        s = str(int("".join(s)) + 1)
        s = [int(i) for i in s]
        return s