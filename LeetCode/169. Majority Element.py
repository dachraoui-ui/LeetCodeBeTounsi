class Solution(object):
    def majorityElement(self, n):
        uni = set(n)
        list_uni = list(uni)
        i = 0
        found = False
        Maj = 0  
        while  not(found):
            if n.count(list_uni[i]) > len(n) / 2:
                found = True
                Maj = list_uni[i]
            i +=1
        return Maj
         
# this solution has time complexity of O(n²) this too much and O(n) space complexity 
#!there is a better one : 

# this is a better solution without extra space and only O(n) time complexity 
class Solution(object):
    def majorityElement(self, n):
        count= 0
        guess = n[0]
        for i in n : 
            if guess == i : 
                count+=1
            elif count == 0 :
                guess = i
            else : 
                count-=1
        return guess

