class Solution:
    def addDigits(self, n: int) -> int:
        str_n = str(n)
        som = 0
        if n // 10 == 0 :
            return n
        while len(str_n) != 1 : 
            som = 0
            for i in str_n : 
                som = som + int(i)
            str_n = str(som)

        return som      

# this the iterative solution this the obvious one using a loop 
# with a time complexity of O(log(n))

#👇
# now the mathimatical solution : view : https://en.wikipedia.org/wiki/Digital_root
class Solution:
    def addDigits(self, n: int) -> int:
        if n // 10 == 0 :
            return n 
        elif n % 9 == 0 :
            return 9
        else : 
            return n % 9
         
s = Solution()
print(s.addDigits(11))

# so in this solution we divide the number and get the mod ( the rest ) , and if the number is divisible by 9 we return 9 
# cause this condition don't apply with 9 

