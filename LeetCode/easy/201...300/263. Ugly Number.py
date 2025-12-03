class Solution:
    def isUgly(self, n: int) -> bool:
        div = n 
        verif = True 
        if n == 0 : 
            return False
        while (div != 1 and  verif):
            if (div % 2 == 0) : 
                div = div // 2
            elif (div % 3 == 0) :
                div = div // 3 
            elif (div % 5 == 0) :
                div = div // 5 
            else : 
                verif = False 
        return verif 
# here is the best solution with time complexity of O(log(n)) and space O(1)