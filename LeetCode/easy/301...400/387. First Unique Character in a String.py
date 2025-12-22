from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_count = Counter(s)
        for i in s_count:
            if s_count[i] == 1 :
                return s.index(i)
        return -1
     
# nothing to explain , undrestand the Counter to ease the undrestand 
        
