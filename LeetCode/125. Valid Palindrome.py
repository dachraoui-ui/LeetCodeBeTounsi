class Solution(object):
    def isPalindrome(self, s):
        #this format make a new string that iterate throw s and check if the element is seperator or not 
        #that element convert it to lower case 
        clean = "".join(c.lower() for c in s if c.isalnum())
        # and here we compare the real clean with the reverse of it clean[::-1] , first argument is the beginning if it's 
        #empty default is 0 , and also the end if it's empty the end = len(clean) -1 and step -1 from the end to beginning 
        return clean == clean[::-1]