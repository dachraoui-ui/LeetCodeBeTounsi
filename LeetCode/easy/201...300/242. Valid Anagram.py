class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
     
# not the best solution but the easier one with O(n logn) time complexity 
# 👇
# here a better solution with O(n) time complexity
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      alph = [0] * 26
      for i in s : 
         alph[ord(i) - ord('a')]+=1
      for j in t : 
         alph[ord(j) - ord('a')]-=1
      for k in alph : 
         if k != 0 : 
            return False 
      return True 


#!test : 
sl = Solution() 
s = 'ahmed'
t = 'ahedm'
print(sl.isAnagram(s,t))
      
      