class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #slice, length=length(s1)
        d1={}
        length=len(s1)
        for e in s1:
            d1[e]=1+d1.get(e,0)
        for l in range(len(s2)):
            r=l
            d2={}
            while r-l<length and r<len(s2):
                d2[s2[r]]=1+d2.get(s2[r],0)
                r+=1
            if d1==d2:
                return True
        return False
