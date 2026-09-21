class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #stack, value and index
        r=[]
        re=[]
        for i in range(len(temperatures) - 1, -1, -1):
            while r and temperatures[i]>=r[-1][0]:
                r.pop(-1)
            if r==[]:
                re.append(0)
            else:
                re.append(r[-1][1]-i)
            r.append([temperatures[i],i])
        re.reverse()
        return re










        