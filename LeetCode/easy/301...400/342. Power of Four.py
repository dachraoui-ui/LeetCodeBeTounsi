class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        bn = bin(n)[2:][::-1]
        if bn.count("1") == 1 and n >= 0:
            if bn.index("1") % 2 == 0: 
                return True 
        return False 
     
# solution without loop or recursion 
# so time complexity is O(1)
# the idea is convert the number to binary then reverse it so you can get the indexes in the right way 
# at first we check if that bin 1's count equal to 1 and it's greater than 0 
# the second check is checking the position of one is't odd or even if it's even we return True 
# ex p :  10000  : you can check that every pow of 4 have 1 in even position in binary 
#         43210