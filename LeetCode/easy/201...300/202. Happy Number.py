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

# todo : explanation : 
# so in this implementation i convert n to a string so i can perferm string and list actions on it 
# so the condition of happy number is that each power 2 digit added together should give a 1 so the result should be 
# 10eN . so the idea is performing the pw 2 of each digits and each number we get we put it in a list l[], 
# and every time we get the res we check if it's in the l or not to not perform an endless loopp 👌