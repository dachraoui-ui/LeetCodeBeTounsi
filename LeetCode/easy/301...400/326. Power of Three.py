class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        M_3 = False 
        if n == 1 :
            return True 
        while (n>=1) : 
            if n % 3 != 0 : 
                return False 
            elif n % 3 == 0 and n // 3 == 1: 
                return True 
            else :
                n = n // 3 
        return False

# solution with loop with O(log n ) time complexity 
class Solution : 
   def isPowerOfThree(self, n: int) -> bool:
      if (n % 3 != 0 or n == 0) and n != 1: 
         return False 
      elif (n % 3 == 0 and n // 3 == 1) or n == 1: 
         return True 
      else :
         return self.isPowerOfThree(n//3)
s = Solution()
n = 21
print(s.isPowerOfThree(n))