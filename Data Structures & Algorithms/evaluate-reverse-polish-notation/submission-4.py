class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        r=[]
        if len(tokens)==1:
            return int(tokens[0])
        for i in range(len(tokens)):
            if tokens[i] not in "+" and tokens[i] not in "-" and tokens[i] not in "*" and tokens[i] not in "/":
                r.append(tokens[i])
            else:
                if tokens[i]=="+":
                    temp=int(r[-2])+int(r[-1])
                    r.pop()
                    r.pop()
                    r.append(temp)
                elif tokens[i]=="-":
                    temp=int(r[-2])-int(r[-1])
                    r.pop()
                    r.pop()
                    r.append(temp)
                elif tokens[i]=="*":
                    temp=int(r[-2])*int(r[-1])
                    r.pop()
                    r.pop()
                    r.append(temp)
                elif tokens[i]=="/":
                    temp=int(int(r[-2])/int(r[-1]))
                    r.pop()
                    r.pop()
                    r.append(temp)
        return r[0]
                


            