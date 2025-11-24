class Solution(object):
    def prefixesDivBy5(self, n):
        res = 0 
        k = len(n)-1
        for i in range (len(n)):
            res = res + n[i] * 2**k
            if res % 5 == 0:
                n[i]=True 
            else : 
                n[i]=False
            k-=1
        return n 
#there is a better one i need to implement it 