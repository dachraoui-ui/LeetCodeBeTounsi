# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0


import random


class Solution:
   def guess(num: int) -> int:
      return random(1,0,-1)
   def guessNumber(self, n: int) -> int:
        end = n
        fst = 1 
        mid = (end + fst)//2
        while (self.guess(mid) != 0  or fst>end ) : 
            mid = (end + fst)//2
            if (self.guess(mid) < 0):
                mid -=1
                end = mid 
            elif (self.guess(mid) > 0):
                mid +=1
                fst = mid 
        return mid 

# this solution uses in the basic binary search cause when you play the game the smartest way to 
# to get the right answer to start decrising the interval of searching and this is what binary search 
# does and for the guess function and self.guess no need to put them , i put them just to prevent my 
# python editor problems of knowing the function guess 