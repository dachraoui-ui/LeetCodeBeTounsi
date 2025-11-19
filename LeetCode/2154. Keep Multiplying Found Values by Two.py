class Solution(object):
    # solution without the dict 
    # time complexity O(n) and space O(n) 
    def findFinalValue(self, nums, original):
        found = True
        while found :
            if original in nums :
                original = original * 2 
            else : 
                found = False
        return original 
    

    #this solution use the dict 
    #but the first solution in better in time complexity and space 
    def findFinalValue(self, nums, original):
        nu = {i: nums[i] for i in range(len(nums))}
        found = True  
        while found : 
            if original in nu.values():
                original = original *2
            else : 
                found = False 
        return original 