class Solution(object):
    def containsDuplicate(self, n):
        i = 0
        n.sort()
        while (i<len(n)-1):
            if n[i] ^ n[i+1] == 0: 
                return True 
            else : 
                i +=1
        return False
# the first solution with O(n logn) time complexity and space complexity equal O(1)
# you can replace the xor ^ symbole with == cause here they do the same effect 

# 👇👇 better solution : 
class Solution(object):
    def containsDuplicate(self, n):
        set_n = set(n)
        return not(len(n) == len(set_n))

# a simpler solution 