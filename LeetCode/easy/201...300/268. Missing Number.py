from typing import List

class Solution:
    def missingNumber(self, n: List[int]) -> int:
        n_sort = [-1] * (len(n)+ 1)
        for i in n:
            n_sort[i] = i
        for j in range(len(n_sort)) :
            if n_sort[j] == -1 : 
                return j
             
# a solution with extra space with O(n) time complexity and O(n) space 
# just creating another array that contains -1 (they say all are positive)
# then arrange them by index in the n_sort array and if we find -1 so that number 
# is missing 
class Solution:
    def missingNumber(self, n: List[int]) -> int:
        real_sum = len(n)
        sum_n = 0 
        for i in range(len(n)):
            sum_n = sum_n + n[i]
            real_sum = real_sum + i
        return real_sum - sum_n
     
# this is a solution of O(n) time complexity and O(1) space 