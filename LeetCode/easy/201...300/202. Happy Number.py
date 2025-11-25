class Solution(object):
    def isHappy(self, n):
        n = str(n)
        l = []
        res = 0
        while (res!=1) : 
            if res in l : 
                return False 
            l.append(int(n))
            res = 0
            for i in n : 
                res = res + int(i)**2
            n = str(res)

