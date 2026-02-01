from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sorted_list = sorted(set(nums))
        n = len(sorted_list)
        if n == 0 : 
            return None
        elif n == 1 : 
            return sorted_list[0]
        elif n == 2 : 
            return sorted_list[1]
        else : 
            return sorted_list[n-3]
         
## this is the first solution using the built in function in python sorted and set 
# this solution has complexity time O(n log n) and space O(n)
# under this , there is a better one with O(n) time complexity 
