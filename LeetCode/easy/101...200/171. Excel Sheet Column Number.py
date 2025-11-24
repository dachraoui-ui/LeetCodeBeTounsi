
class Solution(object):
    def titleToNumber(self, col):
        res = 0 
        l = len(col) - 1
        for i in col : 
            res = res + (26 ** l) * (ord(i) - 64)
            l-=1
        return res 

# you can use this solution to convert any base from 10 to any base just change the '26' 
# starting from getting the length of string and 