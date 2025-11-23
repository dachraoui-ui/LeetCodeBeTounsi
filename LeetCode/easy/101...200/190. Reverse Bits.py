class Solution(object):
    def reverseBits(self, n):
        binary = bin(n)[2:].zfill(32)
        l = 0
        res = 0 
        for i in binary :
            res = res + int(i) * (2 **l)
            l+=1
        return res
     
#here first of all we convert the n number to bin with built in python fonction and we get '0b10...'
#so we slice the two first element from the string by the way the result of bin is string after this step .
# 2 : we use the fonction zfill to fill the missing bits from the left to right with zero cause the quest demand 32bits
# 3 : so without reversing the string , i already the reverse the l means that instead of putting l as length of binary 
# and start from the right to the left , i start from the right and just start from the minimum power 
# 4 : so for every iteration i convert the i in nums to integer and muliply it with 2e(l)
# 5 : and for each iteration i add 1 to the power 