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
    
    
# ! explanation : 
# so at first we create a set it acts like a window so that window should be with length k and if we pass this length we 
# delete the first element of it cause when k = 3 and then the set length = 4 the condition of the distance k break 
# so each time we loop through the array n check if that element is in the set in specific distance k return true , if not 
# we add that number and we also check if we pass the length of k in the n_set .

# ? this solution with O(n) time complexity cause we use one loop and the search in the set is O(1)
# and space complexity O(Min(n,k))
        