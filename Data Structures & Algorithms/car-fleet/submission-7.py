class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #data processing
        r=[]
        for i in range(len(speed)):
            r.append([position[i],speed[i]])
        r.sort(key=lambda x: x[0],reverse=True)

        output=len(position)
        t=(target-r[0][0])/r[0][1]
        for i in range(1,len(r)):
            # if >= target which means it has the same time
            if r[i][0]+t*r[i][1]>=target:
                output-=1
            else:
                #new fleet, new time
                t=(target-r[i][0])/r[i][1]

            
        return output

                
                


