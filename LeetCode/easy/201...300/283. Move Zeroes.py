from typing import List

class Solution:
    def moveZeroes(self, n: List[int]) -> None:
        j = 0 
        for i in range(len(n)):
            if n[i] != 0 : 
                n[j], n[i] = n[i] , n[j]
                j+=1 
        
 # this solution use O(1) means no extra space and with O(n) time complexity 
 # at first we make a simple loop with index i and if that element is diff to 0
 # then we permut between i and j and j goes for the next 0    