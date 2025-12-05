# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
   def firstBadVersion(self, n: int) -> int:
        first = 0
        last = n 
        while (first <= last ) : 
            mid = (first + last )// 2 
            if (isBadVersion(mid)==True and isBadVersion(mid-1)==False):
                return mid 
            elif (isBadVersion(mid)==True ):
                last = mid -1
            else : 
                first = mid + 1
        return -1
   
# the same concepts of binary search and the only added thing is checking if the bad version is true of the mid and the 
# previous isbad mid -1    
   
def isBadVersion(n:int) -> bool : 
      if n // 2 == 0 : 
         return True 
      else : 
         return False    