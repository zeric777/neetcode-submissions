class Solution:
    def isValid(self, s: str) -> bool:
        d={')':'(','}':'{',']':'['}
        r=[]
        for i in range(len(s)):
            if s[i] in d:
                if r and r[-1] ==d[s[i]]:
                    r.pop()
                else:
                    return False
            else:
                r.append(s[i])
        if r==[]:
            return True
        return False


            
