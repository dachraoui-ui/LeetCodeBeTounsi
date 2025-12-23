class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        s_hash = dict()
        if len(s) == 0 : 
            return True 
        while (j < len(t) and i < len(s)):
            if s[i] == t[j]:
                s_hash[i] = t[j]
                i+=1 
            j+=1
        if len(s_hash) != len(s):
            return False
        for k in s_hash : 
            if s_hash[k] != s[k] :
                return False 
        return True 
        
# this my first thougths solution , it would be better it had O(n+m) time complexity with n = len(s) and m = len(t) 
# and O(n) space complexity in my solution i use two pointers to check if the letters in s are in t and each time i get 
# equality i add to the s_hash that letter with the real index of it in t without counting the other non existing letters 
# after that i loop through the s_hash and we check if the letter in s and s_hash in the same index are the same or not , 
# before we did this loop we check the length of the s_hash and s if different or not in the case we found "a" and "b" as inputs 
class Solution:
   def isSubsequence(self, s: str, t: str) -> bool:
         i = 0
         for c in t : 
            if i < len(s) and s[i] == c :
               i+=1
         return i == len(s)     
      
# a simpler solution without using a extra space 
#  another solution but using two pointer without extra space we first start the loop in t 
# and each time we get s[i] == c add 1 to i to check the other letter in s and if the letter didn't exist 
# we complete the loop in t without making the condition i == len(s) True , So we get False 