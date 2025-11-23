class Solution(object):
    def isPalindrome(self, x):
        # solution 1 : in this approch 
        # I convert the number to a string then i make a loop that loop through this string 
        # from the end of it then for every iteration it adds a caracter but in the reverse 
        # then compare them .
        # time complexity O(n)
        # memory complexity O(n)
        strX = str(x)
        strComp = ''
        for i in range(len(strX) -  1 , -1 ,-1 ) : 
            strComp = strComp + strX[i] 
        if strComp == strX : 
            return True 
        else :
            return False 