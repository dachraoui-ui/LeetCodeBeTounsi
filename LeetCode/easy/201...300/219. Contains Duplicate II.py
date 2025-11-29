class Solution(object):
    def containsNearbyDuplicate(self, n, k):
        n_set = set()
        for i in range(len(n)): 
            if(n[i] in n_set):
                return True
            n_set.add(n[i])

            if (len(n_set)>k):
                n_set.remove(n[i-k])       
        return False 
        