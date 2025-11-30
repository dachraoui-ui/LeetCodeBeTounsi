from typing import List
class Solution:
    def summaryRanges(self, n: List[int]) -> List[str]:
        end = 0
        st = 0
        res = []
      # 1: first block :
        if (len(n)==0):
            return n 
        elif (len(n)==1):
            res.append(str(n[0]))
            return res
      # 2 : second block : 
        while ( end < len(n)-1):
            if n[end+1] == n[end] + 1 : 
                end+=1
            else : 
                if n[end] == n[st]:
                    res.append(f"{n[st]}")
                    end+=1
                    st = end
                else : 
                    res.append(f"{n[st]}->{n[end]}")
                    end = end + 1
                    st = end 
      # 3 : third block : 
        if end == st:
            res.append(f"{n[end]}")
        else : 
            res.append(f"{n[st]}->{n[end]}")
        return res

# at first we need two counters the end and start 'st' and the list res to put the result on it :
# 1 : let's start with the first block before we need to check the length of the list if it's 0 we return the empty n 
# and if it's 1 we add the n[0] to res and return res : this block for exeptional cases .
# 2 : for the second block i made a loop that quit when end reach the len(n) - 1 why we made -1 cause if you let it only 
# len(n) the end counter with pass the range , so you will ask what about the last element how to resolve that 
# here third block comes to check the remaining element (last ones) : we made two checks one if it's a single number 
# and one if it's the range of two 
