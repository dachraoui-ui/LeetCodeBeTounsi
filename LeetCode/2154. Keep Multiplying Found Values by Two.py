class Solution(object):
    def findFinalValue(self, nums, original):
        found = True
        while found :
            if original in nums :
                original = original * 2 
            else : 
                found = False
        return original 