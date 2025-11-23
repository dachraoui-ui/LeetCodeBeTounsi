class Solution(object):
    def maxProfit(self, p):
        l = len(p)
        max_pro = 0 
        min_pri = p[0]
        for i in range (l):
            if p[i] < min_pri : 
                min_pri = p[i]
            elif max_pro < p[i] - min_pri :
                max_pro = p[i] - min_pri
                
        return max_pro

 # for a solution O(n) time compexity we gonna fix the min_price and each time the counter i advance 
 # we compare the min_price to the current one if is less we put that value in min_price else we compare the max_profit 
 # with the diff between the current value and min_price if it bigger we change the max_profit to the get the maximum one 
 # each time        