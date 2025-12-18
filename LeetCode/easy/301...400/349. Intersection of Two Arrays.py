from typing import List

class Solution:
    def intersection(self, n1: List[int], n2: List[int]) -> List[int]:
        n1 = set(n1)
        res =[]
        for i in range(len(n2)):
            if n2[i] in n1 : 
                res.append(n2[i])
        n = set(res)
        return list(n)