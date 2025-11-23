class Solution(object):
   def singleNumber(self, nums):
        res = 0
        for n in nums : 
            res ^= n 
        return res 

   # so in this problem you need to know a new concept that is XOR cause it's not used in daily issues "^"
   # that's why people forgot about it so first the main use of xor that he eliminate the double and let the unique element
   # and that works only for an array that contains only 1 unique value and other element are twiced (only 2 not 3)
   # so the main idea how it works is : let's take an array that contains [2,3,2]
   # convert 2 -> to binary : 10 so 2 ^ 3 = 10 ^ 11 = 01 and to the next : 
   # 01 ^ 10 = 11 = 3 in dicimal so that solution works with :
   # O(n) time complexity and also the space 